import random
import math
from src.lab2.Cipher import Cipher


class RSA(Cipher):

    def __init__(self, key_size=1024):
        super().__init__()
        self.key_size = key_size
        self.public_key, self.private_key = self.generate_key_pair()


    def decrypt(self, text):
        pass

    def encrypt(self, text):
        pass
