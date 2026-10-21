"""
:3 <3
"""

def common_letter(text):
    """
    return letter (a-z) which appears the most frequently in text
    :param text: string or list
    """
    text = list(text)

    highest = ('',0)
    for i in range(0,26):
        letter = chr(65+i)
        count = text.count(letter)
        if count > highest[1]:
            highest = (letter, count)

    return highest[0]


def char_set(text):
    """
    return a character set for text
    :param text: string or list
    """
    char_set = list(set(text))

    return sorted(char_set)


def count(text, sort_frequency = True):
    """
    return a character count table
    :param text: string or list
    :param sort_frequency: True for sort by frequency, False for sort alphabetically
    :return: [[string, int]]
    """

    char_set = set(text)
    count_table = [[char, text.count(char)] for char in char_set]

    if sort_frequency:
        count_table.sort(key = lambda x:x[1], reverse = True)
    else:
        count_table.sort(key=lambda x: x[0], reverse = False)

    return count_table


def monogram_frequency(text, sort = True, force_dimension = False, alphabetical = False):
    #works with strings and lists

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    TEXT_LENGTH = len(text)
    count_table = count(text)
    frequency_table = [[i[0], round(i[1]/TEXT_LENGTH, 5)] for i in count_table]

    if force_dimension:
        for item in frequency_table:
            if item[0] not in ALPHABET:
                frequency_table.remove(item)
        keys = [item[0] for item in frequency_table]
        for letter in ALPHABET:
            if letter not in keys:
                frequency_table.append([letter, 0])

    if sort:
        frequency_table.sort(key = lambda x:x[1], reverse = True)

    if alphabetical:
        frequency_table.sort(key=lambda x: x[0])

    return frequency_table