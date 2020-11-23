from unittest import TestCase
from exportAudio import ExportAudio


class TestExportAudio(TestCase):
    def setUp(self):
        self.exp = ExportAudio()
    def test_1(self):
        self.assertEqual(self.exp.export([(10,15), (20,25), (30,60)], "./audio_data_test/ex.ogg"), ['./audio_data_test/cut10-15.mp3','./audio_data_test/cut20-25.mp3','./audio_data_test/cut30-60.mp3',])
    def test_2(self):
        self.assertEqual(len(self.exp.export([(5,20),(40,60),(75,90),(100,125)], "./audio_data_test/dialog.ogg")), 4)