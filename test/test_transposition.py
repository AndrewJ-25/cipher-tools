import pytest
import cipher_tools.transposition as trans

file = open("../corpus/natural-text.txt")
text = file.read()
file.close()

text = "ABCDEFG"
key = [1,0]

print(trans.decrypt(text, key))