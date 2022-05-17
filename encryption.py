import random

def encrypt(message, password):
    random.seed(password)
    output = ""
    for letter in message:
        output += chr(ord(letter) + random.randint(5000, 20000))

    return(output)

def decrypt(message, password):
    random.seed(password)
    output = ""
    for letter in message:
        output += chr(ord(letter) - random.randint(5000, 20000))

    return(output)