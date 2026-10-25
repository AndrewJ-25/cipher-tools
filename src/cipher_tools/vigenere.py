import analysis.ioc as ioc
import analysis.frequency as frequency
import caesar, normalise, statistics

def find_key_length(text, max_len = 10):
    EXPECTED_IOC = 0.0667
    key_lengths = []
    for length in range(3, max_len):
        indices = []  # list to hold the ioc's of each column
        for column in normalise.split_columns(text, length):
            indices.append(ioc.ioc(column))

        mean = statistics.fmean(indices)
        key_lengths.append([length, mean, abs(mean - EXPECTED_IOC)])

    key_lengths.sort(key=lambda x: x[2])  # sort based off closeness to ENGLISH_IOC

    return key_lengths[0][0]


def find_shift(text, n):
    pass


def crack(text):
    pass


def keyword(key):
    """
    find the keyword from a known key
    :param key: [int]
    :return: string
    """
    pass

if __name__ == "__main__":
    pass

