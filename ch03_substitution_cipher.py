#!/usr/bin/python3
import random
#encryption
def substitutionEncrypt(plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz " #alphabet and space
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText: #looping through plain text and getting each index
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText
def substitutionEncryptPass(plainText, paswd):
    key = genKeyFromPass(paswd)
    alphabet = "abcdefghijklmnopqrstuvwxyz " #alphabet and space
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText: #looping through plain text and getting each index
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText
def substitutionDecrypt(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    decrypetdText = ""
    for ch in cipherText:
        idx = key.find(ch)
        decrypetdText += alphabet[idx]
    return decrypetdText
def substitutionDecryptPass(cipherText, paswd):
    key = genKeyFromPass(paswd)
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    decrypetdText = ""
    for ch in cipherText:
        idx = key.find(ch)
        decrypetdText += alphabet[idx]
    return decrypetdText

# testKey1 = "zyxwvutsrqponml kjihgfedcba"
# # testKey2 = "ouwckbjmpzyexa vrltsfgdqihn"

# print(substitutionEncrypt("the sky is blue", testKey1))
# print(substitutionEncrypt("Aratrika RayDowling", testKey2))



#Creating a key

#small function for removing one character from a string
def removeChar(string, idx):
    return string[:idx] + string[idx+1:]

# print(removeChar('abcdefg', 6))

#KEY GENERATING FUNCTION
def keyGen():
    alphabet = "abcdefghijklmnopqrstuvwxyz " #initial 
    key = "" #initial
    for i in range(len(alphabet)-1, -1, -1): #get indices from 26 to 0 backwards
        idx = random.randint(0, i)
        key = key + alphabet[idx]
        alphabet = removeChar(alphabet, idx)
    return key
# print(keyGen())
# print(keyGen())
# print(keyGen())
# print(keyGen())
# print(keyGen())

#Genrating key with a password

#removing duplicates from a string
def removeDuplic(myString):
    newStr = ""
    for ch in myString:
        if ch not in newStr: #recall not in operator 
            newStr = newStr + ch
    return newStr

# print(removeDuplic('topsecret'))
# print(removeDuplic('wonder woman'))

#remove characters in one string from another
def removeMatches(myString, password):
    newStr = ""
    for ch in myString:
        if ch not in password:
            newStr = newStr + ch 
    return newStr

alph = "abcdefghijklmnopqrstuvwxyz "
# print(removeMatches(alph, 'topsecr'))
# print(removeMatches(alph, removeDuplic('topsecret')))

def genKeyFromPass(password):
    alph =  "abcdefghijklmnopqrstuvwxyz "
    password = password.lower() 
    password = removeDuplic(password) #step-1
    lastChar = password[-1]
    lastIdx = alph.find(lastChar)
    afterString = removeMatches(alph[lastIdx+1 : ], password)
    beforeString = removeMatches(alph[ : lastIdx], password)
    key = password + afterString + beforeString
    return key

print(genKeyFromPass('topsecret'))





