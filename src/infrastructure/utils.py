"""Module providing itility functions."""


def divide_into_segments(text: bytes, size: int) -> list[bytes]:
    """
    Get all the sequences of a given length in the text
    :param text: String to get the sequences from
    :param length: The length of the sequences to get
    :return: A list of sequences of the given length
    """

    return [text[i : i + size] for i in range(0, len(text), size)]
