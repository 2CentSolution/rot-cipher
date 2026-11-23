#from rot_cipher import rotate_text

#assert rotate_text("ABC",13) == "NOP"
#assert rotate_text("abc", 13) == "nop"
#assert rotate_text("XYZ", 13) == "KLM"
#assert rotate_text("Hello, World!", 13) == "Uryyb, Jbeyq!"
#assert rotate_text("ABC", 0) == "ABC"

import unittest
from rot_cipher import rotate_text

class TestRotCipher(unittest.TestCase):
    def test_rot13_uppercase(self):
        self.assertEqual(rotate_text("ABC", 13), "NOP")
    def test_rot13_lowercase(self):
        self.assertEqual(rotate_text("abc", 13), "nop")
    def test_wraparound(self):
        self.assertEqual(rotate_text("XYZ", 13), "KLM")
    def test_punctuation(self):
        self.assertEqual(
            rotate_text("Hello, World!", 13), "Uryyb, Jbeyq!")
    def test_zero_rotation(self):
        self.assertEqual(rotate_text("ABC", 0), "ABC")
    def test_alphabet_boundaries(self):
        self.assertEqual(rotate_text("Z", 1), "A")
        self.assertEqual(rotate_text("z", 1), "a")
        self.assertEqual(rotate_text("A", 25), "Z")
        self.assertEqual(rotate_text("a", 25), "z")
