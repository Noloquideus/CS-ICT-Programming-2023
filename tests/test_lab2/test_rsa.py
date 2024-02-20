import unittest
from src.lab2.rsa import RSA


class TestRSA(unittest.TestCase):
    def setUp(self):
        self.rsa = RSA()

    def test_is_prime(self):
        self.assertTrue(self.rsa.is_prime(17))
        self.assertFalse(self.rsa.is_prime(16))

    def test_generate_keypair(self):
        public_key, private_key = self.rsa.generate_keypair()
        self.assertIsInstance(public_key, tuple)
        self.assertIsInstance(private_key, tuple)

    def test_gcd(self):
        self.assertEqual(self.rsa.gcd(14, 21), 7)
        self.assertEqual(self.rsa.gcd(35, 48), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(self.rsa.multiplicative_inverse(3, 11), 4)
        self.assertEqual(self.rsa.multiplicative_inverse(7, 40), 23)

    def test_choose_public_exponent(self):
        phi = 40
        e = self.rsa.choose_public_exponent(phi)
        self.assertTrue(1 < e < phi)

    def test_encrypt_decrypt_combined(self):
        message = "Hello, RSA!"
        cipher_text = self.rsa.encrypt(message)
        decrypted_text = self.rsa.decrypt(cipher_text)
        self.assertEqual(message, decrypted_text)


if __name__ == '__main__':
    unittest.main()
