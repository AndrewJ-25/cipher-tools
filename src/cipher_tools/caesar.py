from src.cipher_tools.analysis import frequency


def shift(text, n):
    """
    shift a string by n letters
    """
    return "".join(chr((ord(c) - 65 + n) % 26 + 65) for c in text)

def crack(text):
    """
    find the most common letter then perform shift
    """
    n = (ord(frequency.common_letter(text)) - 69) % 26

    return shift(text, -n)

if __name__ == "__main__":
    with open("../../corpus/normalised-text.txt") as text:
        text = text.read()

    text = shift(text, 7)
    print(text)
    print(crack(text))