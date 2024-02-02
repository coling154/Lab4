# main.py

from ch03_transposition_cipher import *
from ch03_substitution_cipher import *
"""
1. The Transposition Cipher  0.5%
The sender creates a text message (plaintext) and encrypts it with the transposition cipher and gives the ciphertext to the receiver.
The receiver decrypts the received ciphertext and confirms with the sender that the result matches with the original plaintext.
Document the process (the function calls made by both the sender and receiver, the plaintext and the ciphertext, and the conclusion that the result matches with the plaintext).
You may want to use Google Doc for communication
"""


# person 1
plainText = "Hello, how are you today?"
print("usr1:\t" + plainText)
cipherText = scramble2Encrypt(plainText)
print("\nEncrypting msg with transposition cipher:\t" + scramble2Encrypt(plainText))
# person 2
print("\nDecrypting msg with transposition cipher:\t" + scramble2Decrypt(cipherText))
plainText = "Good, how are you?"
print("\nusr2:\t" + plainText)
print("\nEncrypting msg with transposition cipher:\t" + scramble2Encrypt(plainText))
# person 1
print("\nDecrypting msg with transposition cipher:\n" + scramble2Decrypt(cipherText))
print("\n")


"""
2. The Substitution Cipher (Auto-generated key) 0.5%
Repeat the above process using the substitution cipher and a generated key.
Note that in this task, in addition to coming up with a plaintext, the sender must generate a key using one of the functions below and share it with the receiver.
Document the process (the function calls made by both the sender and receiver, the plaintext, the generated key, and the ciphertext, and the conclusion that the result matches with the plaintext).
"""
secretKey = keyGen()
# User 1 and User 2 share the secret key in person
print("Key is:\t" + secretKey)
# User 1
plainText = "What did you have for lunch today"
print("usr1:\t" + plainText)
cipherText = substitutionEncrypt(plainText, secretKey)
print("\nEncrypting msg with substitution cipher:\t" + cipherText)
# User 2
plainText = substitutionDecrypt(cipherText, secretKey)
print("\nDecrypting msg with substitution cipher:\t" + plainText)
plainText = "Cheese pizza sandwich"
print("usr2:\t" + plainText)
print("\nEncrypting msg with substitution cipher:\t" + cipherText)
# User 1
plainText = substitutionDecrypt(cipherText, secretKey)
print("\nDecrypting msg with substitution cipher:\t" + plainText)
print("\n")


"""
3. The Substitution Cipher (passphrase-based key) 0.5%

Repeat the above process using the substitution cipher and a passphrase.

Note that the sender must come up with a passphrase, generate a key using one of 
the functions below and the passphrase as an argument,
and share the passphrase and the ciphertext with the receiver.
The receiver must recover the plaintext from the given ciphertext and passphrase.
Document the process (the function calls made by both the sender and receiver, the plaintext,
the passphrase, and the ciphertext, and the conclusion that the result matches with the plaintext).
"""
password = "password"
key = genKeyFromPass(password)
print("\nPassword is:\t" + password)
print("\nKey is:\t" + secretKey)

# User 1
plainText = "hello form secret person"
cipherText = substitutionEncryptPass(plainText, password)
print("usr1:\t" + plainText)
print("\nEncrypting msg with substitution cipher with password:\t" + cipherText)
# User 2
plainText = substitutionDecryptPass(cipherText, password)
print("\nDecrypting msg with substitution cipher with password:\t" + plainText)
plainText = "nice secure password"
cipherText = substitutionEncryptPass(plainText, password)
print("usr2:\t" + plainText)
print("\nEncrypting msg with substitution cipher with password:\t" + cipherText)
# User 1
plainText = substitutionDecryptPass(cipherText, password)
print("\nDecrypting msg with substitution cipher with password:\t" + plainText)


"""
4. Re-implementing the Transposition Cipher  0.5%

Re-implement scramble2Encrypt() such that even chars appear before odd chars in the returned ciphertext. Modify scramble2Decrypt() accordingly.
Write a test plan to demonstrate the implementation works for all cases.
"""
# test1
plainText = "Testing 1"
print("Test 1:\t" + plainText)
cipherText = scramble2Encrypt2(plainText)
print("\nEncryptTest1 1:\t" + cipherText)
plainText = scramble2Decrypt2(cipherText)
print("\nDecryptTest 1:\t" + plainText)
# test 2
plainText = "odd chars"
print("\nTest 2:\t" + plainText)
cipherText = scramble2Encrypt2(plainText)
print("\nEncryptTest1 2:\t" + cipherText)
plainText = scramble2Decrypt2(cipherText)
print("\nDecryptTest 2:\t" + plainText)
# test 3
plainText = "even chars"
print("\nTest 3:\t" + plainText)
cipherText = scramble2Encrypt2(plainText)
print("\nEncryptTest1 3:\t" + cipherText)
plainText = scramble2Decrypt2(cipherText)
print("\nDecryptTest 3:\t" + plainText)
# test 4
plainText = "0123456789"
print("\nTest 4:\t" + plainText)
cipherText = scramble2Encrypt2(plainText)
print("\nEncryptTest1 4:\t" + cipherText)
plainText = scramble2Decrypt2(cipherText)
print("\nDecryptTest 4:\t" + plainText)


"""
5. palindrome(s)  1%

Using negative indices to implement a function to test whether a string s is a palindrome. s is a 
palindrome if it reads the same backward as forward, e.g., "madam", "nursesrun", "a", "abba", or "aabbbbaa". Properly document the function.
"""
def is_palindrome(s):
    """
    This function checks for palindromes which are words spelled the same forwards as backwards
     and returns true if it is a palindrome and false if it is not

     :param s: the string you want the check if it is a palindrome
     :type s: str

     :return: returns true if it is a palindrome and false if it is not
     :rtype: bool
    """
    s = s.lower()
    for i in range(len(s) // 2):
        # Compare characters from both ends moving towards the center
        # if string at i index is not at the len - i then is not palindrome
        if s[i] != s[-(i + 1)]:
            return False
    return True
# Test 1
testStr = "racecar"
print("\nTest 1: is \"" + testStr + "\" a palindrome? \t", is_palindrome(testStr))
# Test 2
testStr = "level"
print("\nTest 2: is \"" + testStr + "\" a palindrome? \t",  is_palindrome(testStr))
# Test 3
testStr = "not"
print("\nTest 3: is \"" + testStr + "\" a palindrome? \t", is_palindrome(testStr))







