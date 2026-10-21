import pytest

file = open("../corpus/natural-text.txt")
text = file.read()
file.close()

def test_strip():
    raw = "a b c d!"
    assert print()