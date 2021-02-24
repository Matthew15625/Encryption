import os
import random
import math

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def getMessage(fileName):
    file = open("Functional/"+fileName)
    line = file.readline()
    file.close()
    return line

def calculateOffset(key):
    offset = 0
    for char in key:
        offset += ord(char)
    offset = offset/8
    offset = math.floor(offset)
    offset -= 32
    return offset

def generateKey():
    key = ""
    for i in range(8):
        asc = random.randint(33, 126)
        char = chr(asc)
        key += char
    return key

def encrypt(message, offset):
    try:
        offset = int(offset)
    except:
        offset = calculateOffset(offset)
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
    
def saveMessage(message, fileName):
    file = open("Functional/"+fileName+".txt", "w")
    file.write(message)
    file.close()

def decryptMessage(message, offset):
    try:
        offset = int(offset)
    except:
        offset = calculateOffset(offset)
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

def splitIntoFives(message):
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

def encryption(extended = False):
    fileName = input("What is the name of the file where your message is stored? ")
    originalMessage = getMessage(fileName)

    key = generateKey()
    print("Key:", key)
    encryptedMessage = encrypt(originalMessage, key)

    if extended:
        encryptedMessage = splitIntoFives(encryptedMessage)
    newFileName = input("Enter the name of the new text file where the encrypted message will be stored: ")
    saveMessage(encryptedMessage, newFileName)

def decryption():
    fileName = input("What is the name of the file where your message to be decrypted is? ")
    encryptedMessage = getMessage(fileName)
    key = input("What is the encryption key? ")
    decryptedMessage = decryptMessage(encryptedMessage, key)
    print("Decrypted message:", decryptedMessage)
    input("Press enter to continue...")


def displayMenu():
    while True:
        clear()
        print("Choose an option from the menu below:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Encrypt message using extended encryption")
        print("4. Quit")
        print()

        validAnswer = False
        choice = ""
        while not validAnswer:
            choice = input("Choose an option (1/2/3/4): ")
            if choice in ["1", "2", "3", "4"]:
                validAnswer = True
            else:
                print("Please enter a 1, 2, 3, or 4.")

        if choice == "1":
            #encrypt message
            encryption()
        elif choice == "2":
            #decrypt message
            decryption()
        elif choice == "3":
            #extended encryption
            encryption(extended = True)
        elif choice == "4":
            #quit
            exit()

displayMenu()