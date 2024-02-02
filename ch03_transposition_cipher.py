#!/usr/bin/python3

#encryption 
def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    count = 0
    for ch in plainText:
        if count % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        count = count + 1 # increamented to next position. position starts at 0
    cipherText = oddChars + evenChars
    return cipherText
def scramble2Encrypt2(plainText):
    evenChars = ""
    oddChars = ""
    count = 0
    for ch in plainText:
        if count % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        count = count + 1 # increamented to next position. position starts at 0
    cipherText = evenChars + oddChars
    return cipherText
def scramble2Decrypt2(cipherText):
    if len(cipherText) % 2 == 0:
        splitPoint = len(cipherText) // 2
    else:
        splitPoint = len(cipherText) // 2 + 1

    evenChars = cipherText[:splitPoint]
    oddChars = cipherText[splitPoint:]
    plainText = ""
    for i in range(max(len(evenChars), len(oddChars))):
        if i < len(evenChars):
            plainText += evenChars[i]
        if i < len(oddChars):
            plainText += oddChars[i]
    return plainText



# print(scramble2Encrypt('It was a dark and stormy night'))

#decryption
def scramble2Decrypt(cipherText):
    half_length = len(cipherText) // 2
    evenChars = cipherText[half_length:]
    oddChars = cipherText[:half_length]
    plainText = ""

    for i in range(half_length):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

# print(scramble2Decrypt('twsadr n tryngtI a  akadsom ih'))

def encryptMsg():
    msg = input('Enter a message to encrypt: ')
    cipherText = scramble2Encrypt(msg)
    print("Encrypted msg: ", cipherText)