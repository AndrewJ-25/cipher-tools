"""
SPLITTING:
    Write by rows, read by rows:
        - encrypt and decrypt use same grid construction procedure

    Write by rows, read by columns:
        - Encrypt:
            split columns, join columns
        - Decrypt:
            split blocks, assemble columns

PERMUTATIONS:
    EXAMPLE:
        Key         201
        Plaintext   abc
        Ciphertext  bca

    double encrypting returns to original???
"""

import random
import copy
from . import normalise
from .analysis import fitness

def permute(columns, key):
    """
    scramble columns
    :param columns: []
    :param key: [int]
    :return: []
    """
    return list(map(columns.__getitem__, key))

def encrypt_simple(text, key):
    """
    write by rows, read by columns
    :param text: string
    :param key: [int]
    :return: string
    """
    return

def decrypt_simple(text, key):
    """
    write by rows, read by columns
    :param text: string
    :param key: [int]
    :return: string
    """
    column_size = len(text) // len(key)
    columns = normalise.split_blocks(text, column_size)
    print(columns)
    columns = permute(columns, key)
    plaintext = normalise.assemble_columns(columns)
    return plaintext

def decrypt(text, key):
    """
    write by rows, read by rows
    :param text: string
    :param key: [int]
    :return: string
    """
    columns = normalise.split_columns(text, len(key))
    return normalise.assemble_columns(permute(columns, key))


def climb(text, key_length):
    COUNT_MULTIPLIER = 100
    MARGIN = 0.15
    STEP_DOWN_PROBABILITY = 20

    #set parent key and parent fitness
    parent_key = list(range(key_length))
    parent_fitness = fitness.tetragram_fitness(text)

    counter = 0
    max_count = COUNT_MULTIPLIER * key_length

    while counter < max_count:
        print(counter)

        #generate child key
        child_key = copy.deepcopy(parent_key)
        if bool(random.getrandbits(1)):
            #swap two randomly selected elements
            i = random.randint(0, key_length-1)
            j = random.randint(0, key_length-1)
            child_key[i], child_key[j] = child_key[j], child_key[i]
        else:
            #roll a random number of steps
            i = random.randint(1, key_length)
            child_key = child_key[i:] + child_key[:i]

        # decrypt and find new fitness
        decrypted = decrypt(text, child_key)
        child_fitness = fitness.tetragram_fitness(decrypted)

        can_step_down = random.randint(1, STEP_DOWN_PROBABILITY) == 1
        if child_fitness > parent_fitness or (can_step_down and child_fitness + MARGIN > parent_fitness):
            parent_fitness = child_fitness
            parent_key = copy.deepcopy(child_key)
            counter = 0

        #increment counter
        counter += 1

    return parent_key

if __name__ == "__main__":
    ciphertext = "CBA"
    key = [2, 1, 0]

    plaintext = decrypt(ciphertext, key)

    again = decrypt(plaintext, key)

    print(again)