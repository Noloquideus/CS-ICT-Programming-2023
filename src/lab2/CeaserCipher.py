from Cipher import Cipher


class CeaserCipher(Cipher):

    def __init__(self, shift):
        super().__init__()
        self.shift = shift

    def encrypt(self, text):

        """
        Encrypts the input text using the Caesar cipher with the specified shift.

        Parameters:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """

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

    def decrypt(self, text: str) -> str:
        """
        Decrypts the given text using the Caesar cipher with the specified shift value.

        Parameters:
            text (str): The text to be decrypted.

        Returns:
            str: The decrypted text.
        """

        decrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    decrypted_text += chr((ord(char) - self.shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - self.shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += char
        return decrypted_text

