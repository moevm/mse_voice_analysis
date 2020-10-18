from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


size_cut = 10
precision = 0.005
dictors = {}


def add_dictor(frequency, frequencies):
    for f in dictors.keys():
        if np.abs(frequency - f) < precision:
            dictors[f] += 1
            frequencies.append(f)
            return
    frequencies.append(frequency)
    dictors[frequency] = 1


def manyDictorsIdentification(wav, possible_number=False):
    encoder = VoiceEncoder()
    embed = encoder.embed_utterance(wav, rate=16)
    np.set_printoptions(suppress=True)
    voices = []
    for i in embed:
        if i > 0.05:
            voices.append(i)
    count = 0
    frequency = 0
    frequencies = []
    for i in range(len(voices)):
        count += 1
        frequency += voices[i]
        if count == size_cut:
            frequency /= size_cut
            add_dictor(frequency, frequencies)
            count = 0
            frequency = 0
    count = 0
    for i in dictors.keys():
        if dictors[i] > 1:
            count += 1
    '''
    #Visualisation
    plt.plot(np.arange(start=0, stop=len(frequencies), step=1), frequencies, color='red')
    plt.xlabel('frames')
    plt.ylabel('frequency')
    plt.show()
    '''
    if possible_number:
        return count, len(dictors.keys())
    return count


