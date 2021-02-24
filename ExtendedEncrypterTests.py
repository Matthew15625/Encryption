import unittest
from Encryption import Crypter, Encrypter, ExtendedEncrypter

class ExtendedEncrypterTest(unittest.TestCase):

    def test_splitIntoFives(self):
        extendedEncrypter = ExtendedEncrypter()
        self.assertEqual(extendedEncrypter.splitIntoFives("IT WAS A DARK AND STORMY NIGHT"), "ITWAS ADARK ANDST ORMYN IGHT")

if __name__ == "__main__":
    unittest.main()