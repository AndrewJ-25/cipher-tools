"""
EXAMPLE:
    Key         201
    Plaintext   abc
    Ciphertext  bca

double encrypting returns to original???
"""

import random, normalise

def encrypt(text, key):
    return

def decrypt(text, key):
    """
    :param text: string
    :param key: [int]
    :return: string
    """
    columns = normalise.split_columns(text, len(key))
    columns = list(map(columns.__getitem__, key))
    return normalise.assemble_columns(columns)

def climb():
    return

if __name__ == "__main__":
    ciphertext = "CBA"
    key = [2, 1, 0]

    plaintext = decrypt(ciphertext, key)

    again = decrypt(plaintext, key)

    print(again)