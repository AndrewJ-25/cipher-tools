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


def char_count(text, sort_frequency = True):
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


def letter_count(text, frequency = True, alphabetical = False):
    """
    count the occurrence of each letter of the alphabet in text; forces 26 dimensions
    :param text: string or list
    :param frequency: return count table or frequency table
    :param alphabetical: sort by count or by alphabet
    :return: [[string, int]]
    """

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = list(text)
    text_len = len(text)
    if frequency:
        count_table = [[letter, text.count(letter)] for letter in ALPHABET]
    else:
        count_table = [[letter, text.count(letter)/text_len] for letter in ALPHABET]

    if alphabetical:
        count_table.sort(key=lambda x: x[0])
    else:
        count_table.sort(key=lambda x: x[1], reverse=True)

    return count_table

def ngram_frequency(text, n = 3, alphabetical = False):
    """
    frequency of all ngrams of length n which appear in text
    :param text: string
    :param n: integer
    :param alphabetical: sort by alphabetical or by frequency
    :return: [[string, float]]
    """

    #gather set of all ngrams
    ngrams = []
    length = len(text) - (n-1)

    for i in range(length):
        slice = text[i:i+n]
        if slice not in ngrams:
            ngrams.append(slice)

    #count occurrences of each ngram
    count_table = [[i, text.count(i)] for i in ngrams]
    frequency_table = [[i[0], round(i[1] / length, 5)] for i in count_table]

    #sort table
    if alphabetical:
        frequency_table.sort(key = lambda x:x[0])
    else:
        frequency_table.sort(key=lambda x: x[1], reverse=True)

    return frequency_table

if __name__ == "__main__":
    with open("../../../corpus/normalised-text.txt") as text:
        text = text.read()
    text = "ABCD"
    print(letter_count(text))