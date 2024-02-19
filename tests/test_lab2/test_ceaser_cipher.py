import unittest
from src.lab2.CeaserCipher import CeaserCipher


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        # Test encryption for various shifts
        shifts = [1, 5, 13, 20]

        for shift in shifts:
            cipher = CeaserCipher(shift=shift)

            # Original text
            original_text = "Hello, World!"

            # Encrypt the text
            encrypted_text = cipher.encrypt(original_text)

            # Check if the encrypted text is different from the original text
            self.assertNotEqual(encrypted_text, original_text)

    def test_decrypt(self):
        # Test decryption for various shifts
        shifts = [1, 5, 13, 20]

        for shift in shifts:
            cipher = CeaserCipher(shift=shift)

            # Original text
            original_text = "Hello, World!"

            # Encrypt the text
            encrypted_text = cipher.encrypt(original_text)

            # Decrypt the text
            decrypted_text = cipher.decrypt(encrypted_text)

            # Check if the decrypted text matches the original text
            self.assertEqual(decrypted_text, original_text)

    def test_encrypt_decrypt_combined(self):
        # Test encryption and decryption for various shifts
        shifts = [1, 5, 13, 20]

        for shift in shifts:
            cipher = CeaserCipher(shift=shift)

            # Original text
            original_text = "Hello, World!"

            # Encrypt the text
            encrypted_text = cipher.encrypt(original_text)

            # Decrypt the text
            decrypted_text = cipher.decrypt(encrypted_text)

            # Check if the decrypted text matches the original text
            self.assertEqual(decrypted_text, original_text)

    def test_edge_cases(self):
        # Test with an empty string
        cipher = CeaserCipher(shift=3)
        self.assertEqual(cipher.encrypt(""), "")
        self.assertEqual(cipher.decrypt(""), "")

        # Test with a string containing only non-alphabetic characters
        self.assertEqual(cipher.encrypt("123!@#"), "123!@#")
        self.assertEqual(cipher.decrypt("123!@#"), "123!@#")


if __name__ == '__main__':
    unittest.main()
