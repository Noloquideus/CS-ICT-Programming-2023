from src.lab2.Cipher import Cipher


class VigenereCipher(Cipher):
    def __init__(self, key: str):
        super().__init__()
        self.key = key

    def encrypt(self, text: str) -> str:
        encrypted_text = ""
        key_length = len(self.key)

        for i in range(len(text)):
            char = text[i]
            if char.isalpha():

                shift = ord(self.key[i % key_length].upper()) - ord('A')

                if char.isupper():
                    encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += char

        return encrypted_text

    def decrypt(self, text: str) -> str:
        decrypted_text = ""
        key_length = len(self.key)

        for i in range(len(text)):
            char = text[i]
            if char.isalpha():
                # Determine the shift for the current character in the key
                shift = ord(self.key[i % key_length].upper()) - ord('A')

                # Decrypt the character
                if char.isupper():
                    decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += char

        return decrypted_text
