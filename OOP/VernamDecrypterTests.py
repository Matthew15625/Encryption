import unittest
from Encryption import VernamDecrypter

class VernamDecrypterTests(unittest.TestCase):

    def test_decrypt(self):
        message = "1809191800"
        otp = "PLUTO"
        decrypter = VernamDecrypter()
        self.assertEqual(decrypter.decrypt(message, otp), "HELLO")

if __name__ == "__main__":
    unittest.main()