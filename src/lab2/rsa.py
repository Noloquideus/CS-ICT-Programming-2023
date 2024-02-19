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

    def decrypt(self, text):
        pass

    def encrypt(self, text):
        pass
