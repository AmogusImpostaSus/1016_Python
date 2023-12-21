import random

class Encryptor:
    def __init__(self, key=None):
        if key is None:
            key = random.randint(1, 100)
        self.key = key
        self.encrypted_value = None

    def _encrypt(self, value):
        return value + self.key

    def encrypt(self, value):
        self.encrypted_value = self._encrypt(value)

    def decrypt(self):
        if self.encrypted_value is not None:
            return self.encrypted_value - self.key
        else:
            return None

    def __repr__(self):
        if self.encrypted_value is not None:
            return f"Зашифрованное значение: {self.encrypted_value}, Расшифрованное значение: {self.decrypt()}"
        else:
            return "Значение не зашифровано."

if __name__ == "__main__":
    encryptor = Encryptor()
    number_to_encrypt = 42
    encryptor.encrypt(number_to_encrypt)
    print(encryptor)
