import math
import random
import string

class Crypter():
    def __init__(self):
        super().__init__()

    def getMessage(self, fileName):
        
        file = open("OOP/"+fileName)
        line = file.readline()
        file.close()
        return line

    def calculateOffset(self, key):
        offset = 0
        for char in key:
            offset += ord(char)
        offset = offset/8
        offset = math.floor(offset)
        offset -= 32
        return offset
    
    def saveMessage(self, message, fileName):
        file = open("OOP/"+fileName+".txt", "w")
        file.write(message)
        file.close()


class Encrypter(Crypter):
    def __init__(self):
        super().__init__()

    def generateKey(self):
        key = ""
        for i in range(8):
            asc = random.randint(33, 126)
            char = chr(asc)
            key += char
        return key

    def encrypt(self, message, offset):
        try:
            offset = int(offset)
        except:
            offset = self.calculateOffset(offset)
        encryptedMessage = ""
        for char in message:
            if char == " ":
                encryptedMessage += " "
            else:
                asc = ord(char)
                asc += offset
                if asc > 126:
                   asc -= 94
                encryptedMessage += str(chr(asc))
        return encryptedMessage

class Decrypter(Crypter):
    def __init__(self):
        super().__init__()

    def decryptMessage(self, message, offset):
        try:
            offset = int(offset)
        except:
            offset = self.calculateOffset(offset)
        decryptedMessage = ""
        for char in message:
            if char == " ":
                decryptedMessage += " "
            else:
                asc = ord(char)
                asc -= offset
                if asc < 33:
                    asc += 94
                decryptedMessage += chr(asc)
        return decryptedMessage

class ExtendedEncrypter(Encrypter):

    def splitIntoFives(self, message):
        noSpaces = message.replace(" ", "")
        noSpaces = list(noSpaces)
        length = len(noSpaces)
        splitMessage = ""
        for i in range(length):
            if i % 5 == 0:
                if i != 0:
                    splitMessage += " "
            splitMessage += noSpaces[i]
        return splitMessage

class VernamEncrypter(Crypter):

    def generateOTP(self, length):
        otp = ""
        for i in range(length):
            otp += random.choice(list(string.ascii_letters + string.digits))
        return otp

    def encrypt(self, message, otp):
        encryptedMessage = ""
        for i in range(len(message)):
            ascii1 = ord(message[i])
            ascii2 = ord(otp[i])
            XORed = ascii1 ^ ascii2
            hexChar = hex(XORed)
            hexChar = str(hexChar)
            hexChar = hexChar[2:]
            if len(hexChar) == 1:
                hexChar = "0" + hexChar
            encryptedMessage += hexChar
        return encryptedMessage


class VernamDecrypter(Crypter):
    
    def decrypt(self, message, otp):
        decryptedMessage = ""
        try:
            for i in range(int(len(message)/2)):
                ascii1 = int(message[i*2:i*2+2], 16)
                ascii2 = ord(otp[i])
                decryptedMessage += chr(ascii1 ^ ascii2)
            return decryptedMessage
        except:
            return None