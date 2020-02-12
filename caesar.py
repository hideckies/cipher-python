"""
Caesar cipher
"""

import sys
import getpass


def caesar(plaintext, key):
    """
    plaintext: original data
    key: number of character shift
    """
    ciphertext = ""

    for ch in plaintext:
        asc = ord(ch)   # convert to ASCII
        if 65 <= asc <= 90:
            num = asc - 65  # A=0, B=1, ..., Z=25
            shift_asc = (num + key) % 26
            cipherchar = chr(shift_asc + 65)
            ciphertext += cipherchar
        elif 97 <= asc <= 122:
            num = asc - 97  # a=0, b=1, ..., z=25
            shift_asc = (num + key) % 26
            cipherchar = chr(shift_asc + 97)
            ciphertext += cipherchar
        else:
            sys.stderr("Error: alphabet only")

    return ciphertext


if __name__ == "__main__":
    plaintext = getpass.getpass()
    print("")
    print("Created: {}".format(caesar(plaintext, 3)))
