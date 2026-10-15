import frequency

def shift(text, n):
    return "".join(chr((ord(c) - 65 + n) % 26 + 65) for c in text)

def crack(text):
    n = (ord(frequency.common_letter(text)) - 69) % 26

    return shift(text, -n)