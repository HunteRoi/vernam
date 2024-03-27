"""Module providing the feature to attack cipher text to find plaintext."""

from collections import Counter

from src.infrastructure.kasiski import find_key_size
from src.infrastructure.utils import divide_into_segments
from src.application.commands.decrypt import decrypt


def attack(cipher_text: bytes, print_msg: lambda *args, **kwargs: None) -> str:
    """Function to attack the cipher text to find the plaintext."""
    key_size = find_key_size(cipher_text)
    print_msg(f"potential key size: {key_size}")

    key_letters: list[bytes] = []
    segments = divide_into_segments(cipher_text, key_size)
    for i in range(key_size):
        significant_letters: list[bytes] = [
            segment[i] for segment in segments if i < len(segment)
        ]
        frequencies = Counter(significant_letters)
        most_frequent_byte: bytes = max(frequencies, key=frequencies.get)

        most_frequent_letter = chr(most_frequent_byte ^ ord("e"))
        print_msg(f"potential key letter at position {i}: {most_frequent_letter}")

        key_letters.append(most_frequent_letter)

    key = "".join(key_letters)
    print_msg(f"potential key: {key}")

    return decrypt(cipher_text, key)
