from Cipher import Cipher


class CeaserCipher(Cipher):

    def __init__(self, shift):
        super().__init__()
        self.shift = shift

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    encrypted_text += chr((ord(char) + self.shift - ord('A')) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) + self.shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, **kwargs):
        pass
