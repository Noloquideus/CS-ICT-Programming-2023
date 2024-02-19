import unittest
from src.lab2.VigenereCipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_decrypt_combined(self):
        cipher = VigenereCipher("key")

        test_word = "Hello"
        enc_word = cipher.encrypt(test_word)
        denc_word = cipher.decrypt(enc_word)

        self.assertEqual(test_word, denc_word)

    def test_empty_string(self):
        cipher = VigenereCipher("key")

        test_word = ""
        enc_word = cipher.encrypt(test_word)
        denc_word = cipher.decrypt(enc_word)

        self.assertEqual(test_word, denc_word)

    def test_encrypt_decrypt_special_characters(self):
        cipher = VigenereCipher("key")

        test_word = "!@#$%^&*()_+"
        enc_word = cipher.encrypt(test_word)
        denc_word = cipher.decrypt(enc_word)

        self.assertEqual(test_word, denc_word)


if __name__ == '__main__':
    unittest.main()
