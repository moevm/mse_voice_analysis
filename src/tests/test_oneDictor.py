from unittest import TestCase
from oneDictor import oneDictorIdentification

class Test(TestCase):
    def test_one_dictor_identification(self):
        self.assertEqual(oneDictorIdentification("../../res/audio_data_test/1.mp3", "../../res/audio_data_test/2.mp3"), 1)
        self.assertEqual(oneDictorIdentification("../../res/audio_data_test/think.mp3", "../../res/audio_data_test/money.mp3"), 1)
        self.assertEqual(oneDictorIdentification("../../res/audio_data_test/think.mp3", "../../res/audio_data_test/2.mp3"), 0)
        self.assertEqual(oneDictorIdentification("../../res/audio_data_test/money.mp3", "../../res/audio_data_test/1.mp3"), 0)

        self.assertEqual(
            oneDictorIdentification("../../res/Belyaev1.mp3", "../../res/Belyaev2.mp3"), 1)
        self.assertEqual(
            oneDictorIdentification("../../res/Eric1.mp3", "../../res/Eric2.mp3"), 1)
        self.assertEqual(
            oneDictorIdentification("../../res/Oblomov1.mp3", "../../res/Oblomov2.mp3"), 1)
        self.assertEqual(
            oneDictorIdentification("../../res/Puchkov1.mp3", "../../res/Puchkov2.mp3"), 1)
        self.assertEqual(
            oneDictorIdentification("../../res/trump1.mp3", "../../res/trump4.mp3"), 1)
        self.assertEqual(
            oneDictorIdentification("../../res/Wylsa1.mp3", "../../res/Wylsa2.mp3"), 1)
        self.assertEqual(
            oneDictorIdentification("../../res/ValeryAlbertovich1.mp3", "../../res/ValeryAlbertovich2.mp3"), 1)

        self.assertEqual(
            oneDictorIdentification("../../res/Puchkov1.mp3", "../../res/trump2.mp3"), 0)
        self.assertEqual(
            oneDictorIdentification("../../res/Wylsa1.mp3", "../../res/ValeryAlbertovich2.mp3"), 0)
        self.assertEqual(
            oneDictorIdentification("../../res/Oblomov1.mp3", "../../res/Belyaev1.mp3"), 0)
        self.assertEqual(
            oneDictorIdentification("../../res/ValeryAlbertovich1.mp3", "../../res/Puchkov2.mp3"), 0)
        self.assertEqual(
            oneDictorIdentification("../../res/Eric1.mp3", "../../res/Wylsa2.mp3"), 0)


