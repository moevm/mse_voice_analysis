import unittest
from pathlib import Path
from resemblyzer import preprocess_wav
from manyDictors import many_dictors


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.identification = many_dictors()

    def test1(self):
        wav = preprocess_wav(Path("audio_data_test", "ex.ogg"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 3 <= possible)

    def test2(self):
        wav = preprocess_wav(Path("audio_data_test", "clown.ogg"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 1 <= possible)

    def test3(self):
        wav = preprocess_wav(Path("audio_data_test", "dialog.ogg"))
        confident, possible = self.identification.manyDictorsIdentification(wav, True)
        self.assertTrue(confident <= 2 <= possible)


if __name__ == '__main__':
    unittest.main()
