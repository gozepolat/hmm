from ml import decoders
from ds.pgm import HiddenMarkov
import unittest


class HiddenMarkovTest(unittest.TestCase):
    def test_hmm_invalid(self):
        self.assertFalse(HiddenMarkov().is_valid())
        self.assertFalse(HiddenMarkov().is_valid())
        self.assertFalse(HiddenMarkov().is_valid())
        self.assertFalse(HiddenMarkov().is_valid())


if __name__ == '__main__':
    unittest.main()
