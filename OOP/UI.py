from Encryption import Encrypter, Decrypter, ExtendedEncrypter, VernamEncrypter, VernamDecrypter
import os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

# checks the validity of a given file
def checkFileIsValid(name):
    try:
        # checks to see if the file has an extension
        extension = name.split(".")[1]
        # checks the extension is .txt
        if extension != "txt":
            print("Only .txt files can be accepted.")
            return False
    except:
        print("Please include the file extension.")
        return False
    # checks the file exists
    try:
        file = open("OOP/"+name)
        file.close()
    except:
        print("File does not exist. Please make sure it is in the OOP directory.")
        return False
    return True

# user has selected an encryption option
def encrypt(extended = False, vernam = False):
    encrypter = Encrypter()
    if extended:
        # user selected extended encryption
        encrypter = ExtendedEncrypter()
    elif vernam:
        # user selected Vernam encryption
        encrypter = VernamEncrypter()
    # gets name of file conataining message to be encrypted
    validFile = False
    while not validFile:
        fileName = input("What is the name of the file where your message is stored (including extension)? ")
        validFile = checkFileIsValid(fileName)
    originalMessage = encrypter.getMessage(fileName)
    encryptedMessage = ""
    if not vernam:
        # standard or extended encryption
        key = encrypter.generateKey()
        print("Key:", key)
        encryptedMessage = encrypter.encrypt(originalMessage, key)
        if extended:
            encryptedMessage = encrypter.splitIntoFives(encryptedMessage)
    else:
        # Vernam encryption
        # generate a one-time pad
        otp = encrypter.generateOTP(len(originalMessage))
        print("One-time pad:", otp)
        print("The otp will also get saved to a file so you can copy it.")
        encryptedMessage = encrypter.encrypt(originalMessage, otp)
    newFileName = input("Enter the name of the new text file where the encrypted message will be stored (without extension): ")
    encrypter.saveMessage(encryptedMessage, newFileName)
    encrypter.saveMessage(otp, "otp")

# user selected a decryption option
def decrypt(vernam = False):
    decrypter = Decrypter()
    if vernam:
        # user selected Vernam decryption
        decrypter = VernamDecrypter()
    # gets the name of the file containing the message to be decoded
    validFile = False
    while not validFile:
        fileName = input("What is the name of the file where your message to be decrypted is (with extension)? ")
        validFile = checkFileIsValid(fileName)
    encryptedMessage = decrypter.getMessage(fileName)
    decryptedMessage = ""
    if not vernam:
        key = input("What is the encryption key? ")
        decryptedMessage = decrypter.decryptMessage(encryptedMessage, key)
    else:
        # gets the one-time pad from the user
        validOTP = False
        otp = ""
        while not validOTP:
            otp = input("What is the one-time pad? ")
            if len(otp) < len(encryptedMessage)/2:
                print("OTP is too short to decrypt the message.")
                answer = input("Return to menu (Y/N)? ")
                answer = answer.lower()
                if answer == "y":
                    return
            else:
                validOTP = True
        decryptedMessage = decrypter.decrypt(encryptedMessage, otp)
        if decryptedMessage is None:
            print("Invalid encrypted message. Must be in hex.")
            input("Press enter to return to the menu...")
            return
    print("Decrypted message:", decryptedMessage)
    input("Press enter to continue...")

def displayMenu():
    print("Choose an option from the menu below:")
    print("1. Encrypt message")
    print("2. Decrypt message")
    print("3. Encrypt message using extended encryption")
    print("4. Encrypt message with Vernam cipher")
    print("5. Decrypt message with Vernam cipher")
    print("6. Quit")
    print()

# program start

# makes an infinite loop - can be stopped throught the menu
while True:
    # clears the screen
    clear()
    # displays the menu, with 5 encryptiom/decryption options, and an option to quit
    displayMenu()
    # get the users choice
    validAnswer = False
    choice = ""
    while not validAnswer:
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            validAnswer = True
        else:
            print("Please enter a 1, 2, 3, 4, 5 or 6.")

    if choice == "1":
        # encrypt message
        encrypt()
    elif choice == "2":
        # decrypt message
        decrypt()
    elif choice == "3":
        # extended encryption
        encrypt(extended = True)
    elif choice == "4":
        # Vernam encryption
        encrypt(vernam = True)
    elif choice == "5":
        # Vernam decryption
        decrypt(vernam = True)
    elif choice == "6":
        # quit
        exit()
