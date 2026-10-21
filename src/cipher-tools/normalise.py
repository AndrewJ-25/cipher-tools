def strip(text, spaces=False, force_case=True, digits=False):
    """
    remove unwanted characters; letters converted to upper-case by default
    :param text: String
    :param spaces: Boolean
    :param force_case: Boolean
    :param digits: Boolean
    :return: String
    """
    allowed = [chr(65+i) for i in range(26)]
    if spaces:
        allowed.append(" ")
    if digits:
        allowed += list(range(10))

    print(allowed)
    if force_case:
        return [char.upper() for char in text if char in allowed]
    else:
        return [char for char in text if char in allowed]

def split_blocks(text, n, padding=False, padding_character="X"):
    """
    splits text into blocks of size n, preserving character sequence
    :param text: string
    :param n: integer
    :param padding: boolean (pad uneven block)
    :param padding_character: string
    :return: list
    """

    if padding:
        text += padding_character * (n - text%n)

    text = list(text)
    split_text = []
    block = []
    while len(text) > 0:
        if len(block) < n:
            block.append(text.pop(0))
        else:
            split_text.append(block)
            block = []

    return split_text

def split_columns(text, n, padding=False, padding_character="X"):
    return

if __name__ == "__main__":
    strip("blob")
