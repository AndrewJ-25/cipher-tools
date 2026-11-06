import numpy as np
from pathlib import Path

#necessary for loading linguistic data from text file, filepath relative to this module
MODULE_DIR = Path(__file__).resolve().parent
FILEPATH_TRIGRAM_FREQUENCY = "linguistic_data/trigram_frequency.txt"
FILEPATH_TRIGRAM_FREQUENCY_LOGS = "linguistic_data/trigram_frequency_logs.txt"
FILEPATH_TETRAGRAM_FREQUENCY = "linguistic_data/tetragram_frequency.txt"
FILEPATH_TETRAGRAM_FREQUENCY_LOGS = "linguistic_data/tetragram_frequency_logs.txt"

def load_data(filepath):
    with open(filepath) as data:
        data = data.readlines()
        table = {}
        for line in data:
            column = line.split()
            table[column[0]] = float(column[1])
    return table

def cosine_angle(vec1, vec2):
    """
    Calculate the cosine of the angle between two vectors of any dimension. Using this formula:
        cos(theta) = dot(U, V) / square_root(dot(U, U) * dot(V, V))
    :param vec1: [float]
    :param vec2: [float]
    :return: float
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    dot_product = np.dot(vec1, vec2)
    magnitude_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cosine = dot_product / magnitude_product

    return cosine

def tetragram_fitness(text):
    DEFAULT_LOG = -12 # Default log for unseen tetragrams
    tetragram_expected_logs = load_data(FILEPATH_TETRAGRAM_FREQUENCY_LOGS)

    num_tetragrams = len(text) - 3  # Total number of tetragrams in text (not necessarily unique)
    if num_tetragrams <= 0:
        return float('-inf')  # No tetragrams, return very negative fitness score

    logs_sum = 0
    for i in range(num_tetragrams):
        tetragram = text[i:i + 4]  # Extract tetragram
        # Get the frequency from the English frequency table or use the default
        log = tetragram_expected_logs.get(tetragram, DEFAULT_LOG)
        logs_sum += log

    # Normalize by dividing by the total number of tetragrams
    return logs_sum / num_tetragrams

if __name__ == "__main__":
    print(load_data(FILEPATH_TETRAGRAM_FREQUENCY_LOGS))