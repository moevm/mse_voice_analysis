import unittest
from pathlib import Path
from speechRecognition import SpeechRecognition
from manyDictors import SeveralSpeakers


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.recognition = SpeechRecognition()
        self.identification = SeveralSpeakers()

    def test1(self):
        path = Path("../../res/audio_data_test", "test1.wav")
        result = self.recognition.recognize_speech(str(path))
        self.assertEqual("hello", result)

    def test2(self):
        path = Path("../../res/audio_data_test", "test2.wav")
        result = self.recognition.recognize_speech(str(path))
        print(result)
        self.assertEqual("London is the capital of Great Britain", result)

    def test3(self):
        path = Path("../../res/audio_data_test", "test3.wav")
        result = self.recognition.recognize_speech(str(path))
        print(result)
        self.assertEqual("three hundred bucks", result)

    def test4(self):
        path = Path("../../res/audio_data_test", "test2.mp3")
        self.identification.several_speakers_identification(path, recognition=True, export=True, min_duration=1)
        res_file = open(str(path) + str('.txt'))
        result = res_file.readline()
        self.assertEqual('Speaker #1 00:00:London is the capital of Great Britain\n', result)


if __name__ == '__main__':
    unittest.main()
