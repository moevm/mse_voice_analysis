from resemblyzer import VoiceEncoder, preprocess_wav
from speechRecognition import SpeechRecognition
from exportAudio import ExportAudio
import numpy as np
import os
import soundfile as sf
from mutagen.mp3 import MP3, HeaderNotFoundError


class SeveralSpeakers:
    def __init__(self):
        self.splits = []
        self.speakers = []
        self.timing = []
        self.min_duration = 3
        self.path = ''
        self.speakers_number = 0
        self.recognized_text = ''
        self.metric = []
        self.old_closest = 0
        self.rate = 1

    def recognize_audio(self, language, paths, export):
        recognizer = SpeechRecognition(language)
        res_file = open('../res/' + str(self.path).replace('\\', '_') + '/recognized.txt', "w")
        print('Recognition started')
        for i in range(len(paths)):
            self.recognized_text += 'Speaker #' + str(self.timing[self.splits[i][0]])
            count = 0
            for m in self.metric[i]:
                if m < 0.75:
                    count += 1
            self.recognized_text += ' (confidence percentage - ' +  str((1 - float(count) / len(self.metric[i])) * 100) + "%)"
            self.recognized_text += ' %02d:%02d: ' % divmod(self.splits[i][0], 60)
            self.recognized_text += recognizer.recognize_speech(paths[i]) + '\n'
            print('Recognition status: ' + str(i + 1) + '/' + str(len(paths)) + '...')
            if not export:
                os.remove(paths[i])
        res_file.write(self.recognized_text)
        res_file.close()

    def get_splits(self):
        tmp = 0
        splits = []
        for i in range(len(self.timing) - 1):
            if self.timing[i] != self.timing[i + 1]:
                if i - tmp <= self.min_duration:
                    continue
                if i + self.min_duration >= len(self.timing):
                    continue
                if self.timing[i + self.min_duration] != self.timing[i+1]:
                    continue
                if self.timing[i + self.min_duration] == self.timing[tmp]:
                    continue
                splits.append((tmp, i+1))
                tmp = i + 1
        splits.append((tmp, len(self.timing) + 1))
        return splits

    def clear(self):
        self.speakers_number = len(self.speakers)
        for i in range(len(self.speakers)):
            if len(self.speakers[i]) < self.min_duration:
                self.speakers_number -= 1
                for j in range(len(self.timing)):
                    if self.timing[j] == i + 1:
                        if j > 0:
                            self.timing[j] = self.timing[j - 1]

    def add_speaker(self, embedding, precision=0.63):
        closest = 0
        closest_precision = 0
        for i in range(len(self.speakers)):
            sum_of_precisions = 0
            for j in range(len(self.speakers[i])):
                sum_of_precisions += self.speakers[i][j] @ embedding
            if len(self.speakers[i]) > 0:
                common_precision = sum_of_precisions / len(self.speakers[i])
                if common_precision > closest_precision:
                    closest_precision = common_precision
                    closest = i

        if closest_precision < precision:
            self.speakers.append([embedding])
            self.timing.append(len(self.speakers))
            self.metric.append([])
            self.old_closest = len(self.speakers) - 1
        else:
            self.timing.append(closest + 1)
            self.speakers[closest].append(embedding)
            if closest == self.old_closest:
                self.metric[len(self.metric) - 1].append(closest_precision)
            else:
                self.metric.append([closest_precision])
                self.old_closest = closest

    def several_speakers_identification(self, path, min_duration=3, return_splits=False, export=False,
                                        recognition=False, language='en-En'):
        self.min_duration = min_duration
        self.path = path
        wav = preprocess_wav(path)
        encoder = VoiceEncoder()
        _, embed, slices = encoder.embed_utterance(wav, return_partials=True, rate=1)
        np.set_printoptions(suppress=True)
        try:
            self.rate = MP3(path).info.length / len(embed)
        except HeaderNotFoundError:
            f = sf.SoundFile(path)
            self.rate = (len(f) / f.samplerate) / len(embed)
        for i in range(len(embed)):
            self.add_speaker(embed[i])
        self.clear()
        print('Found %d speakers' % self.speakers_number)
        for i in range(self.speakers_number):
            print('Speaker ' + str(i) + ': ' + str(len(self.speakers[i])) + 's')
        self.splits = self.get_splits()
        if recognition or export:
            paths = ExportAudio.export(self.splits, self.path, self.rate)
            if recognition:
                self.recognize_audio(language, paths, export)
        if return_splits:
            return self.speakers_number, self.splits
        return self.speakers_number
