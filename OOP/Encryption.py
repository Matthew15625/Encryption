import math
import random
import string

# contains general functionality that most encrypters/decrypters uses
class Crypter():
    def __init__(self):
        super().__init__()

    def getMessage(self, fileName):
        # opens the file containing the message to retrieve
        file = open("OOP/"+fileName)
        # reads the first line
        line = file.readline()
        # then closes the file
        file.close()
        return line

    def calculateOffset(self, key):
        # calculates the offset factor for the caesar cipher using the key provided
        offset = 0
        # loops through each character in the key
        for char in key:
            # converts the character to ASCII, then adds it to the offset
            offset += ord(char)
        # divides the offset by 8
        offset = offset/8
        # rounds it down to the nearset integer
        offset = math.floor(offset)
        # subtracts 32
        offset -= 32
        return offset
    
    def saveMessage(self, message, fileName):
        # opens the files to write, creates a new file if there isnt already one with that name
        file = open("OOP/"+fileName+".txt", "w")
        file.write(message)
        file.close()

# Class for caesar cipher encryption
class Encrypter(Crypter):
    def __init__(self):
        super().__init__()

    # generates a random key of length 8
    def generateKey(self):
        key = ""
        # loops 1-8
        for i in range(8):
            # gets a random number between 33 and 126 (inclusive)
            asc = random.randint(33, 126)
            # converts that number to a character
            char = chr(asc)
            # and adds it to the key
            key += char
        return key

    # encrypts the given message, and can take either a key or an offset
    def encrypt(self, message, keyOrOffset):
        # checks to see if an offset has been given
        offset = 0
        try:
            # if this works, then an offset has been given
            offset = int(keyOrOffset)
        except:
            # the check didnt work, so a key was given. This calculates the offset using the key
            offset = self.calculateOffset(keyOrOffset)
        # initialize the encrypted message
        encryptedMessage = ""
        # loops through the given message
        for char in message:
            # if the current character is a space, then don't encrypt it. Just add it to the encrypted message
            if char == " ":
                encryptedMessage += " "
            else:
                # if the character isn't a space, then encrypt it
                # start by converting it to ASCII
                asc = ord(char)
                # add the offset to the ASCII value
                asc += offset
                # if the new value is more thsn 126, it would be an invalid character. To fix this, subract 94 from the value
                if asc > 126:
                   asc -= 94
                # convert the new ASCII value to a character, and add it to the encrypted message
                encryptedMessage += str(chr(asc))
        return encryptedMessage

# Class for caesar cipher decryption
class Decrypter(Crypter):
    def __init__(self):
        super().__init__()

    #decrypts the given message
    def decryptMessage(self, message, keyOrOffset):
        # checks to see if an offset has been given
        offset = 0
        try:
            # if this works, then an offset has been given
            offset = int(keyOrOffset)
        except:
            # the check didnt work, so a key was given. This calculates the offset using the key
            offset = self.calculateOffset(keyOrOffset)
        # initializes the decrypted message
        decryptedMessage = ""
        # loops through each character in the message
        for char in message:
            # if the current character is a space, then don't decrypt it. Just add it to the decrypted message
            if char == " ":
                decryptedMessage += " "
            else:
                # if the character isn't a space, then decrypt it
                #convert the character to ASCII
                asc = ord(char)
                #take away the offset
                asc -= offset
                #if the offset is less than 33, then it is an invalid character. To fix this, add 94
                if asc < 33:
                    asc += 94
                # convert the new ASCII value to a character and add it to the decrypted message
                decryptedMessage += chr(asc)
        return decryptedMessage

# Class for extended caesar cipher encryption
class ExtendedEncrypter(Encrypter):

    # splits the given message into words of length 5
    def splitIntoFives(self, message):
        # takes out all the spaces
        noSpaces = message.replace(" ", "")
        # converting the string to a list
        noSpaces = list(noSpaces)
        # gets the length of the list
        length = len(noSpaces)
        # initializes a new message
        splitMessage = ""
        # this loop adds a space every 5 characters
        # loops the from 0 to the length of the list
        for i in range(length):
            # if i is divisible by 5
            if i % 5 == 0:
                # and if its not the first iteration
                if i != 0:
                    # then add a space to the new message
                    splitMessage += " "
            # add the current character from the list to the new message
            splitMessage += noSpaces[i]
        return splitMessage

# Class for encryption using the Vernam cipher
class VernamEncrypter(Crypter):

    # generates a one-time pad
    def generateOTP(self, length):
        otp = ""
        #loops for the length given
        for i in range(length):
            #gets a random digit, uppcase or lowercase letter, and adds it to the otp
            otp += random.choice(list(string.ascii_letters + string.digits))
        return otp

    # encrypts using Vernam cipher
    def encrypt(self, message, otp):
    # initializes encrypted message
        encryptedMessage = ""
        # loops through the length of the message
        for i in range(len(message)):
            # gets the ASCII value of the current character of the message
            ascii1 = ord(message[i])
            # gets the ASCII value of the current character of the otp
            ascii2 = ord(otp[i])
            # applies one value to another using the btiwise xor operation
            XORed = ascii1 ^ ascii2
            # turns the new ASCII value to a hex character
            hexChar = hex(XORed)
            # formats the hex character
            hexChar = str(hexChar)
            hexChar = hexChar[2:]
            if len(hexChar) == 1:
                hexChar = "0" + hexChar
            # adds the hex character to the encrypted message
            encryptedMessage += hexChar
        return encryptedMessage

# Class for decrypting a message with Vernam cipher
class VernamDecrypter(Crypter):
    
    # decrypts the given message
    def decrypt(self, message, otp):
        # initializes the decrypted message
        decryptedMessage = ""
        # uses try as some of the lines of code might throw an error. This would happen if the message the user is trying to decrypt is invalid - not using hex.
        try:
            #loops throught the message (each hex number takes two characters, so the length is divived by 2)
            for i in range(int(len(message)/2)):
                # gets the ASCII value of the current hex number
                ascii1 = int(message[i*2:i*2+2], 16)
                # gets the ASCII value of the current otp character
                ascii2 = ord(otp[i])
                # applies one value to another using the bitwise XOR operator
                # converts it to a character
                # and adds it to the decrypted message
                decryptedMessage += chr(ascii1 ^ ascii2)
            return decryptedMessage
        except:
            return None
