import frequency

def ioc(text):
    """
    calculate the index of coincidence of a piece of text. length must be >= 2
    :param text: string
    :return: float
    """
    length = len(text)
    if length >= 2:
        char_set = frequency.char_set(text)
        sum = 0
        for char in char_set:
            count = text.count(char)
            sum += count * (count - 1)

        return sum / (length * (length - 1))

    else:
        return 0

if __name__ == "__main__":
    print(ioc(""))