import unittest
from pathlib import Path
from resemblyzer import preprocess_wav
from manyDictors import many_dictors


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.identification = many_dictors()

    def test1(self):
        wav = preprocess_wav(Path("../../res/audio_data_test", "ex.mp3"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 3 <= possible)

    def test2(self):
        wav = preprocess_wav(Path("../../res/audio_data_test", "clown.mp3"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 1 <= possible)

    def test3(self):
        wav = preprocess_wav(Path("../../res/audio_data_test", "dialog.mp3"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 2 <= possible)

    def test4(self):
        wav = preprocess_wav(Path("../../res", "Belyaev2.mp3"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 1 <= possible)

    def test5(self):
        wav = preprocess_wav(Path("../../res", "OblomovAndPuchkov1.mp3"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 2 <= possible)

    def test6(self):
        wav = preprocess_wav(Path("../../res", "OblomovAndPuchkov2.mp3"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 2 <= possible)

    def test7(self):
        wav = preprocess_wav(Path("../../res", "WylsaAndDroider1.mp3"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 2 <= possible)

    def test8(self):
        wav = preprocess_wav(Path("../../res", "trump1.mp3"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 1 <= possible)




if __name__ == '__main__':
    unittest.main()
