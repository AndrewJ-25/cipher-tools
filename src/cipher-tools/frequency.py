def common_letter(text):
    text = list(text)

    highest = ('',0)
    for i in range(0,26):
        letter = chr(65+i)
        count = text.count(letter)
        if count > highest[1]:
            highest = (letter, count)

    return highest[0]

def set(text):
    #works with strings and lists

    char_set = []
    for i in text:
        if i not in char_set:
            char_set.append(i)

    return sorted(char_set)

def count(text, sort = True):
    #works with strings and lists

    char_set = set(text)
    count_table = [[char, text.count(char)] for char in char_set]

    if sort:
        count_table.sort(key = lambda x:x[1], reverse = True)

    return count_table