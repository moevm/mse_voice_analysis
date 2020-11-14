from unittest import TestCase
from oneDictor import oneDictorIdentification

class Test(TestCase):
    def test_one_dictor_identification(self):
        self.assertEqual(oneDictorIdentification("../../res/audio_data_test/1.mp3", "../../res/audio_data_test/2.mp3"), 1)
        self.assertEqual(oneDictorIdentification("../../res/audio_data_test/think.mp3", "../../res/audio_data_test/money.mp3"), 1)
        self.assertEqual(oneDictorIdentification("../../res/audio_data_test/think.mp3", "../../res/audio_data_test/2.mp3"), 0)
        self.assertEqual(oneDictorIdentification("../../res/audio_data_test/money.mp3", "../../res/audio_data_test/1"
                                                                                        ".mp3"), 0)
