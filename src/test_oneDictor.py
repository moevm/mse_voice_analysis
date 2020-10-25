from unittest import TestCase
from oneDictor import oneDictorIdentification

class Test(TestCase):
    def test_one_dictor_identification(self):
        self.assertEqual(oneDictorIdentification("1.wav", "2.wav"), 1)
        self.assertEqual(oneDictorIdentification("think.wav", "money.wav"), 1)
        self.assertEqual(oneDictorIdentification("think.wav", "2.wav"), 0)
        self.assertEqual(oneDictorIdentification("money.wav", "1.wav"), 0)