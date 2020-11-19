from resemblyzer import VoiceEncoder, preprocess_wav
from speechRecognition import SpeechRecognition
from exportAudio import ExportAudio
import numpy as np

import os


class SeveralSpeakers:
    def __init__(self):
        self.splits = []
        self.speakers = []
        self.timing = []
        self.min_duration = 3
        self.path = ''
        self.speakers_number = 0
        self.recognized_text = ''

    def recognize_audio(self, language, paths, export):
        recognizer = SpeechRecognition(language)
        res_file = open(str(self.path) + str('.txt'), "a")
        print('Recognition started')
        for i in range(len(paths)):
            self.recognized_text += '\nSpeaker #' + str(self.timing[self.splits[i][0]])
            self.recognized_text += ' %02d:%02d:' % divmod(self.splits[i][0], 60)
            self.recognized_text += recognizer.recognize_speech(paths[i])
            print('Recognition status: ' + str(i + 1) + '/' + str(len(paths)) + '...')
            if not export:
                os.remove(paths[i])
        res_file.write(self.recognized_text)

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
        splits.append((tmp, len(self.timing)))
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

    def add_speaker(self, embedding, precision=0.65):
        closet = -1
        closet_precision = 0
        for i in range(len(self.speakers)):
            sum_of_precisions = 0
            for j in range(len(self.speakers[i])):
                sum_of_precisions += self.speakers[i][j] @ embedding
            if len(self.speakers[i]) > 0:
                common_precision = sum_of_precisions / len(self.speakers[i])
                if common_precision > precision:
                    if common_precision > closet_precision:
                        closet_precision = common_precision
                        closet = i
        if closet == -1:
            self.speakers.append([embedding])
            self.timing.append(len(self.speakers))
        else:
            self.timing.append(closet + 1)
            self.speakers[closet].append(embedding)

    def several_speakers_identification(self, path, min_duration=3, return_splits=False, export=False,
                                        recognition=False, language='en-En'):
        self.min_duration = min_duration
        self.path = path
        wav = preprocess_wav(path)
        encoder = VoiceEncoder()
        _, embed, slices = encoder.embed_utterance(wav, return_partials=True, rate=1.16)
        np.set_printoptions(suppress=True)
        for i in range(len(embed)):
            self.add_speaker(embed[i])
        self.clear()
        print('Found %d speakers' % self.speakers_number)
        for i in range(self.speakers_number):
            print('Speaker ' + str(i) + ': ' + str(len(self.speakers[i])) + 's')
        self.splits = self.get_splits()
        if recognition or export:
            paths = ExportAudio.export(self.splits, self.path)
            if recognition:
                self.recognize_audio(language, paths, export)
        if return_splits:
            return self.speakers_number, self.splits
        return self.speakers_number
