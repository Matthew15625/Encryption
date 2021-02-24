import unittest
from Encryption import Crypter, Encrypter

class EncrypterTests(unittest.TestCase):

    def test_getMessage(self):
        encrypter = Encrypter()
        self.assertEqual(encrypter.getMessage("sample.txt"), "Somewhere in la Mancha, in a place whose name I do not care to remember, a gentleman lived not long ago, one of those who has a lance and ancient shield on a shelf and keeps a skinny nag and a greyhound for racing.")

    def test_calculateOffset(self):
        encrypter = Encrypter()
        self.assertEqual(encrypter.calculateOffset(">f5j;[H9"), 43)

    def test_encryptMessage(self):
        encrypter = Encrypter()
        self.assertEqual(encrypter.encrypt("IT WAS A DARK AND STORMY NIGHT", 3), "LW ZDV D GDUN DQG VWRUP\ QLJKW")
        self.assertEqual(encrypter.encrypt("IT WAS A DARK AND STORMY NIGHT", "zz$"), "LW ZDV D GDUN DQG VWRUP\ QLJKW")
    
    def test_saveMessage(self):
        encrypter = Encrypter()
        testMessage = "Test"
        encrypter.saveMessage(testMessage, "testFile")
        testFile = open("testFile.txt")
        loadedMessage = testFile.readline()
        testFile.close()
        self.assertEqual(testMessage, loadedMessage)


if __name__ == '__main__':
    unittest.main()