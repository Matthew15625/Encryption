import unittest
from Encryption import Crypter, Decrypter

class DecrypterTests(unittest.TestCase):

    def test_decryptMessage(self):
        decrypter = Decrypter()
        self.assertEqual(decrypter.decryptMessage("LWZDV DGDUN DQGVW RUP\Q LJKW", 3), "ITWAS ADARK ANDST ORMYN IGHT")
        self.assertEqual(decrypter.decryptMessage("LWZDV DGDUN DQGVW RUP\Q LJKW", "zz$"), "ITWAS ADARK ANDST ORMYN IGHT")

if __name__ == "__main__":
    unittest.main()