import unittest
from Encryption import VernamEncrypter

class VernamEncrypterTests(unittest.TestCase):
    
    def test_encrypt(self):
        encrypter = VernamEncrypter()
        message = "HELLO"
        otp = "PLUTO"
        encrypted = "1809191800"
        self.assertEqual(encrypter.encrypt(message, otp), encrypted)

if __name__ == "__main__":
    unittest.main()