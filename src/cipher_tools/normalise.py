def strip(text, allow_spaces=False, force_upper_case=True, allow_digits=False):
    """
    remove unwanted characters; letters converted to upper-case by default
    :param text: String
    :param allow_spaces: Boolean
    :param force_upper_case: Boolean
    :param allow_digits: Boolean
    :return: String
    """
    allowed = [chr(65+i) for i in range(26)]
    if allow_spaces:
        allowed.append(" ")
    if allow_digits:
        allowed += list(range(10))

    if force_upper_case:
        text = text.upper()
        return "".join([char for char in text if char in allowed])
    else:
        return "".join([char for char in text if char.upper() in allowed])

def split_blocks(text, n, padding=False, padding_character="X"):
    """
    splits text into blocks of size n, preserving character sequence
    :param text: string
    :param n: integer
    :param padding: boolean (pad uneven block)
    :param padding_character: string
    :return: [string]
    """

    if padding:
        text += padding_character * ((n - len(text)%n)%n)

    text = list(text)
    split_text = []
    block = ""
    while len(text) > 0:
        if len(block) < n:
            block += text.pop(0)
        else:
            split_text.append(block)
            block = ""


    split_text.append(block)

    return split_text

def split_columns(text, n, padding=False, padding_character="X"):
    """
    split text into n columns
    :param text: string
    :param n: integer
    :param padding: boolean
    :param padding_character: string
    :return: [string]
    """
    if padding:
        text += padding_character * ((n - len(text)%n)%n)

    columns = ["" for _ in range(n)]
    for i in range(len(text)):
        columns[i % n] += text[i]
    return columns

def assemble_columns(columns):
    """
    assemble a list of columns
    :param columns: [string]
    :return: string
    """
    text = ""
    for pos in range(len(columns[0])):
        for column in columns:
            # clunky!! fix later
            try:
                text += column[pos]
            except:
                pass
    return text

if __name__ == "__main__":
    with open("../../corpus/natural-text.txt") as text:
        text = text.read()

    print(text)
    stripped_text = strip(text)
    blocks = split_blocks("ABCDEF", 1, padding=True)
    columns = split_columns("ABCDEFG", 3, padding=True)
    reassembled = assemble_columns(columns)
    print(columns)
    print(reassembled)
