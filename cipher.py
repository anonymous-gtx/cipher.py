letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def user():
    print("Welcome to anonymous encryption and decryption tool.")
    print("\n *************************************************\n")
    choice = input("Type 'e' or 'E' for encryption or 'd' or 'D' for decryption: ")
    message = input("Enter a text you want to encrypt or decrypt: ")
    message=message.replace(' ', '')
    message = message.upper()
    if choice == "e" or choice == "E":
        key = int(input("Enter the key you want: "))
        encrypt(message,key)
    else :
        if choice == "d" or choice == "D":
            key = int(input("Enter the key you want: "))
            decrypt(message,key)
        else :
            print("Oops!! 'Something went wrong... ")
            print("Please try again.")
            print("\n *************************************************\n")
            user()
def encrypt(message, key):
    print("\n *************************************************\n")
    encrypt_message = ''
    for i in message:
        locate = key + letters.index(i)
        locate %= 26
        encrypt_message += letters[locate]
    print("Your encryption is complete and here is your encrypted message :", encrypt_message)   
def decrypt(message, key):
    print("\n *************************************************\n")
    decrypt_message = ''
    for i in message:
        locate = letters.index(i) -key
        locate %= 26
        decrypt_message += letters[locate]
    print("Your decryption is complete and here is your decrypted message :", decrypt_message)
user()
