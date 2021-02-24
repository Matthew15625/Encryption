from Encryption import Encrypter, Decrypter, ExtendedEncrypter
import os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def encrypt(extended = False):
    encrypter = Encrypter()
    if extended:
        encrypter = ExtendedEncrypter()
    fileName = input("What is the name of the file where your message is stored? ")
    originalMessage = encrypter.getMessage(fileName)
    key = encrypter.generateKey()
    print("Key:", key)
    encryptedMessage = encrypter.encrypt(originalMessage, key)
    if extended:
        encryptedMessage = encrypter.splitIntoFives(encryptedMessage)
    newFileName = input("Enter the name of the new text file where the encrypted message will be stored: ")
    encrypter.saveMessage(encryptedMessage, newFileName)

def decrypt():
    decrypter = Decrypter()
    fileName = input("What is the name of the file where your message to be decrypted is? ")
    encryptedMessage = decrypter.getMessage(fileName)
    key = input("What is the encryption key? ")
    decryptedMessage = decrypter.decryptMessage(encryptedMessage, key)
    print("Decrypted message:", decryptedMessage)
    input("Press enter to continue...")

def displayMenu():
    print("Choose an option from the menu below:")
    print("1. Encrypt message")
    print("2. Decrypt message")
    print("3. Encrypt message using extended encryption")
    print("4. Quit")
    print()

while True:
    clear()
    displayMenu()
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
        encrypt()
    elif choice == "2":
        #decrypt message
        decrypt()
    elif choice == "3":
        #extended encryption
        encrypt(extended = True)
    elif choice == "4":
        #quit
        exit()
