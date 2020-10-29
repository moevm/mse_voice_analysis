from unittest import TestCase
from oneDictor import oneDictorIdentification

class Test(TestCase):
    def test_one_dictor_identification(self):
        self.assertEqual(oneDictorIdentification("./audio_data_test/1.wav", "./audio_data_test/2.wav"), 1)
        self.assertEqual(oneDictorIdentification("./audio_data_test/think.wav", "./audio_data_test/money.wav"), 1)
        self.assertEqual(oneDictorIdentification("./audio_data_test/think.wav", "./audio_data_test/2.wav"), 0)
        self.assertEqual(oneDictorIdentification("./audio_data_test/money.wav", "./audio_data_test/1.wav"), 0)
