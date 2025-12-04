import pytest

def detect_sequences(lower: int, higher: int):
    """
    Finds numbers in a range that consist of repeating sequences.

    Args:
        lower (int): Lower bound of the range.
        higher (int): Upper bound of the range.

    Returns:
        list: List of numbers containing repeating sequences.
    """
    found = []
    for number in range(lower, higher + 1):
        s = str(number)
        length = len(s)
        for i in range(2, length + 1):
            if length % i != 0:
                continue
            seq_len = length // i
            seqs = [s[j*seq_len:(j+1)*seq_len] for j in range(i)]
            if seqs and all(x == seqs[0] for x in seqs):
                found.append(number)
                break
    return found

@pytest.mark.parametrize("rng,expected", [
    ((11, 22), [11, 22]),
    ((95, 115), [99, 111]),
    ((998, 1012), [999, 1010]),
    ((1188511880, 1188511890), [1188511885]),
    ((222220, 222224), [222222]),
    ((1698522, 1698528), []),
    ((446443, 446449), [446446]),
    ((38593856, 38593862), [38593859]),
    ((565653, 565659), [565656]),
    ((824824821, 824824827), [824824824]),
    ((2121212118, 2121212124), [2121212121]),
    ((123123123, 123123129), [123123123]),
])
def test_sequence_detector_cases(rng, expected):
    lower, higher = rng
    assert detect_sequences(lower, higher) == expected