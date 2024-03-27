"""Kasiski module."""

from collections import Counter
import functools
import math
import operator

from src.infrastructure.utils import divide_into_segments


def find_key_size(text: bytes) -> int:
    """Approximate the key size based on Kasiski examination of the text."""

    gcds = []
    for sequence_size in range(2, 6):
        repetitive_sequences = get_repetitive_sequences(text, sequence_size)
        distances_between_repetitions = calculate_distances_between_sequences(
            text, sequence_size, repetitive_sequences
        )
        gcds.append(calculate_gcd(distances_between_repetitions))
    return max(gcds)


def calculate_gcd(distances_between_repetitions: dict[bytes, list[int]]) -> int:
    """Calculate the greatest common divisor of the distances between repetitions."""

    packed_distances = functools.reduce(
        operator.iconcat, distances_between_repetitions.values(), []
    )

    return math.gcd(*packed_distances)


def calculate_distances_between_sequences(
    text: bytes, sequence_size: int, repetitive_sequences: dict[bytes, list[int]]
) -> dict[bytes, list[int]]:
    """Calculate the distances between repetitions of a sequence."""

    sequence_positions = {
        sequence: [
            i for i in range(len(text)) if text[i : i + sequence_size] == sequence
        ]
        for sequence in repetitive_sequences
    }

    distances_between_repetitions = {
        sequence: [
            positions[j] - positions[i]
            for i in range(len(positions))
            for j in range(i + 1, len(positions))
        ]
        for sequence, positions in sequence_positions.items()
    }

    return distances_between_repetitions


def get_repetitive_sequences(text: bytes, sequence_size: int) -> dict[bytes, int]:
    """Get the repetitive sequences in the text."""

    segments = divide_into_segments(text, sequence_size)
    repetitive_sequences = Counter(segments)
    repetitive_sequences = {k: v for k, v in repetitive_sequences.items() if v > 1}
    return repetitive_sequences
