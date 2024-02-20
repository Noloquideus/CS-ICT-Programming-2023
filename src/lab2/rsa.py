import random
import math

from src.lab2.Cipher import Cipher


class RSA(Cipher):

    def __init__(self, key_size=1024):
        super().__init__()
        self.key_size = key_size
        self.public_key, self.private_key = self.generate_keypair()

    def generate_keypair(self):

        """
        Generates a key pair for encryption and decryption.
        Parameters:
            self: the object instance
        Returns:
            tuple: a tuple containing the public key (e, n) and the private key (d, n)
        """

        p = self.generate_prime(self.key_size)
        q = self.generate_prime(self.key_size)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.choose_public_exponent(phi)
        d = self.multiplicative_inverse(e, phi)
        return (e, n), (d, n)

    @staticmethod
    def is_prime(num, test_iterations=10):

        """
        Check if a number is prime using the Miller-Rabin primality test.
        Args:
            num (int): The number to be checked for primality.
            test_iterations (int): The number of iterations for the Miller-Rabin test. Default is 10.
        Returns:
            bool: True if the number is prime, False otherwise.
        """

        if num < 2:
            return False

        for _ in range(test_iterations):
            a = random.randint(2, num - 2)
            if pow(a, num - 1, num) != 1:
                return False
        return True

    def generate_prime(self, bits):

        """
        Generate a prime number with a specified number of bits.
        Parameters:
            self (object): The object instance.
            bits (int): The number of bits for the prime number.
        Returns:
            int: The generated prime number.
        """

        while True:
            num = random.getrandbits(bits)
            if self.is_prime(num):
                return num

    @staticmethod
    def gcd(a, b):
        """
        Calculate the greatest common divisor of two integers using the Euclidean algorithm.
        Args:
            a: An integer representing the first number.
            b: An integer representing the second number.
        Returns:
            An integer representing the greatest common divisor of 'a' and 'b'.
        """
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def multiplicative_inverse(a, m):
        """
        Calculate the multiplicative inverse of a number 'a' modulo 'm'.

        :param a: The number for which the multiplicative inverse is to be calculated.
        :param m: The modulo value.
        :return: The multiplicative inverse of 'a' modulo 'm'.
        """
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def choose_public_exponent(self, phi):
        """
          Chooses a public exponent for the given phi value using a random selection method.

          Parameters:
              phi (int): The phi value for which the public exponent is chosen.

          Returns:
              int: The chosen public exponent.
          """
        e = random.randint(2, phi - 1)
        while self.gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
        return e

    def encrypt(self, message):
        """
        Encrypts a message using the given public key.
        Parameters:
            message (str): The message to be encrypted.
        Returns:
            list: The encrypted cipher text as a list of integers.
        """
        e, n = self.public_key
        cipher_text = [pow(ord(char), e, n) for char in message]
        return cipher_text

    def decrypt(self, cipher_text):
        """
        Decrypts the cipher text using the private key.
        Parameters:
            cipher_text (list): The list of cipher text to be decrypted.
        Returns:
            str: The decrypted plain text.
        """
        d, n = self.private_key
        plain_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
        return plain_text
