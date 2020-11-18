


from pydub import AudioSegment
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

class fileDistribution:
    def __init__(self):
        self.size_cut = 1
        self.precision = 0.003
        self.dictors = {}

    def splitFile(self, timeMarks):
        for i in range(len(timeMarks)-1):
            t1 = timeMarks[i] * 1000  # Works in milliseconds
            t2 = timeMarks[i+1] * 1000
            if i > len(timeMarks):
                return

            newAudio = AudioSegment.from_file("./audio_data_test/ex.ogg")
            newAudio = newAudio[t1:t2]
            newFileName = str(t1/1000) + '_' + str(t2/1000) + '.mp3'
            print(newFileName)
            newAudio.export('./audio_data_test/' + newFileName, format="mp3")

    def identify_dictor(self, frequency):
        min_diff = 1000
        dictor = 0
        for i in self.dictors.keys():
            difference = np.abs(i - frequency)
            if difference < min_diff:
                min_diff = difference
                dictor = i
        return self.dictors[dictor][0]

    def add_dictor(self, frequency, frequencies):
        for f in self.dictors.keys():
            if np.abs(frequency - f) < self.precision:
                self.dictors[f][1] += 1
                frequencies.append(f)
                return
        frequencies.append(frequency)
        self.dictors[frequency] = [len(self.dictors), 1]

    def dictorsIdentification(self, wav, possible_number=False):
        encoder = VoiceEncoder()
        _, embed, slices = encoder.embed_utterance(wav, return_partials=True, rate=2)
        np.set_printoptions(suppress=True)
        voices = []
        for i in embed:
            voices.append(np.average(i))
        print(len(voices))
        count = 0
        frequency = 0
        frequencies = []
        for i in range(len(voices)):
            if i > 0.02:
                count += 1
                frequency += voices[i]
                if count == self.size_cut:
                    frequency /= self.size_cut
                    self.add_dictor(frequency, frequencies)
                    count = 0
                    frequency = 0
        count = 0
        for i in self.dictors.keys():
            if self.dictors[i][1] > 5:
                count += 1
        # Visualisation
     #   plt.plot(np.arange(start=0, stop=len(frequencies), step=1), frequencies, color='red')
     #   plt.xlabel('frames')
     #   plt.ylabel('frequency')
     #   plt.show()
        timeMarks = []
        currentVoice = 0
        frames = 0.5
        for i in voices:
            print(frames, ": ", self.identify_dictor(i))
            if self.identify_dictor(i) != 0 and currentVoice != self.identify_dictor(i):
                currentVoice = self.identify_dictor(i)
                timeMarks.append(frames)
            frames += 0.5
        timeMarks.append(frames)
        print(timeMarks)
        self.splitFile(timeMarks)
        if possible_number:
            return count, len(self.dictors.keys())
        return count


if __name__ == '__main__':
    identification = fileDistribution()
    wav = preprocess_wav(Path("audio_data_test", "ex.ogg"))
    identification.dictorsIdentification(wav, True)
