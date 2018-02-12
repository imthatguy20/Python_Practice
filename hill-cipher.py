#!/usr/bin/python

"""
Lab 2:Hill Cipher
Goal: Create a program that implements Hill cipher
Creator: Jerry Haynes
"""
def get_key():
    key = raw_input().upper()
    return key
def get_msg():
    msg = raw_input().upper()
    return msg
import sys
print (sys.argv)

def hill(msg, key, decrypt=False):
    from math import sqrt
    n = int(sqrt(len(key)))
    if n * n != len(key):
        raise Exception("Invalid key length, should be square-root-able like")

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?,-;|'
    print "[ALPHA LENGTH]: ", len(alpha)
    tonum = dict([(alpha[i], i * 1) for i in range(len(alpha))])
    print
    "[PLAINTEXT]", msg
    # Pad the message with spacess if necessary
    if len(msg) % n > 0:
        msg += '|' * (n - (len(msg) % n))

    # Construct our key matrix
    keylist = []
    for a in key:
        keylist.append(tonum[a])

    keymatrix = []
    for i in range(n):
        keymatrix.append(keylist[i * n: i * n + n])

    from numpy import matrix
    from numpy import linalg

    keymatrix = matrix(keymatrix).round().T

    if decrypt:
        determinant = linalg.det(keymatrix).round()
        print "[DETERMINANT]", determinant
        if determinant == 0:
            raise Exception("Determinant ZERO, CHANGE THE KEY!")
        elif determinant % len(alpha) == 0:
            raise Exception("Determinant divisible by ALPHA LENGTH, CHANGE THE KEY!")

        inverse = []
        keymatrix = matrix(keymatrix.getI() * determinant).round()

        invdeterminant = 0
        for i in range(10000):
            if (determinant * i % len(alpha)) == 1:
                invdeterminant = i
                break

        print "[INVERTED DETERMINANT]", invdeterminant

        for row in keymatrix.getA() * invdeterminant:
            newrow = []
            for i in row:
                newrow.append(i.round() % len(alpha))
            inverse.append(newrow)

        keymatrix = matrix(inverse)

        print "[DECIPHERING]: ", msg
    else:
        print
        "[ENCIPHERING]: ", msg

    print "[MATRIX]\n", keymatrix



    # Main loop
    from string import join
    out = ''
    for i in range(len(msg) / n):
        lst = matrix([[tonum[a]] for a in msg[i * n:i * n + n]])
        result = keymatrix * lst
        out += ''.join([alpha[int(result.A[j][0]) % len(alpha)] for j in range(len(result))])

    return out

decision = ""
while decision is not "1" and decision is not "2":
	print "Would you like to encrypt or decrypt a message?"
	print "1 - Encrypt message"
	print "2 - Decrypt Message"
	print "\nDecision:"
	decision = raw_input()

if decision == "1":
    print"\nEncrypt Message:"

    print "Enter key:"
    key = get_key()
    print "Enter the message you would like to encrypt."
    msg = get_msg()
    print "The message you entered was: %s\n" %msg
    cipherText = hill(msg, key)
    print "[Encrypted Text]: |%s|\n" %cipherText

elif decision == "2":
    print "\nDecrypt Message:"
    print "Enter key:"
    key = get_key()
    print "Enter the message you would like to decrypt."
    msg = get_msg()
    print "The message you entered was: %s" %msg
    cipherText = hill(msg, key)
    decipherText = hill(cipherText, key, True)
    if decipherText.find('|') > -1: decipherText = decipherText[:decipherText.find('|')]
    print "[DECIPHERED TEXT]: |%s|\n" %decipherText
    if (msg == decipherText):
        print
        "[ALGORITHM] CORRECT"
    else:
        print
        "[ALGORITHM] INCORRECT"

