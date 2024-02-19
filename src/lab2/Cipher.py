from abc import ABC, abstractmethod


class Cipher(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def encrypt(self, text):
        pass

    @abstractmethod
    def decrypt(self, text):
        pass
