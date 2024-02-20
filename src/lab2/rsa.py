import random
import math

from src.lab2.Cipher import Cipher


class RSA(Cipher):

    def __init__(self):
        super().__init__()

    @staticmethod
    def is_prime(num, test_iterations=10):
        if num < 2:
            return False

        for _ in range(test_iterations):
            a = random.randint(2, num - 2)
            if pow(a, num - 1, num) != 1:
                return False
        return True

    def generate_prime(self, bits):
        while True:
            num = random.getrandbits(bits)
            if self.is_prime(num):
                return num

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def multiplicative_inverse(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def choose_public_exponent(self, phi):
        e = random.randint(2, phi - 1)
        while self.gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
        return e

    def decrypt(self, text):
        pass

    def encrypt(self, text):
        pass
