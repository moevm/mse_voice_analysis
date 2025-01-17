import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
from pathlib import Path



class oneDictor:


    def __init__(self):
        self.result = 0
        self.cSample = ''
        self.mainFile = ''

    @property
    def get_result(self):
        return self.result

    def oneDictorIdentification(self, cSample, mainFile):
        print('[-i] --> Identify Dictor')
        avg1 = 0.0
        avg2 = 0.0

        fpath = Path(cSample)
        wav = preprocess_wav(fpath)

        encoder = VoiceEncoder()
        embed = encoder.embed_utterance(wav)
        np.set_printoptions(precision=3, suppress=True)
        embedNew = []

        for i in embed:
            if i != 0.0:
                embedNew.append(i)

        for s in embedNew:
            avg1 = avg1 + s

        fpath = Path(mainFile)
        wav = preprocess_wav(fpath)

        encoder = VoiceEncoder()
        embed = encoder.embed_utterance(wav)
        np.set_printoptions(precision=3, suppress=True)
        embedNew2 = []

        for i in embed:
            if i != 0.0:
                embedNew2.append(i)

        for s in embedNew2:
            avg2 = avg2 + s

        self.result = abs((avg2 / len(embedNew2)) - (avg1 / len(embedNew)))
        print(self.result)
        if (self.result < 0.002):
            print("Match!")
            # print("\033[33m\033[1m {}".format("Match!"))
            return 1
        else:
            print("These are different voices")
            # print("\033[33m\033[1m {}".format("These are different voices"))
            return 0

