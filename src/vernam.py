"""
Vernam cipher
"""

import getpass
import random


def vernam(plaintext):
    ciphertext = ""
    b_text = binary_conversion(plaintext)
    k_text = random_key(b_text)

    text_length = len(b_text)
    for i in range(text_length):
        xor = int(b_text[i]) ^ int(k_text[i])
        ciphertext += str(xor)

    return ciphertext


def binary_conversion(txt):
    binary_text = ""

    for ch in txt:
        asc = ord(ch)   # char -> ASCII
        bin_text = bin(asc)  # ASCII -> binary
        binary_text += bin_text[2:]

    return binary_text


def random_key(btext):
    random_text = ""
    key_length = len(btext)

    for i in range(key_length):
        rnum = random.randint(0, 1)
        random_text += str(rnum)

    return random_text


if __name__ == "__main__":
    plaintext = getpass.getpass()
    ciphertext = vernam(plaintext)
    print(ciphertext)
