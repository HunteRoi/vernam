"""Module providing functions to sanitize text."""

import re
from unidecode import unidecode


def remove_diacritics(text):
    """
    Remove diacritics.
    Only the diacritics are removed, not the whole character.
    The character 'à' becomes 'a'.
    """
    return unidecode(text)


def sanitize_to_alpha(text):
    """
    Sanitize the given string to only lowercase alphabetic characters.

    All characters are converted to lowercase.
    Characters with diacritics are converted to the corresponding
    alphabetic character.
    All remaining non-alphabetic characters are removed.
    """
    return re.sub(r"[^a-z]", "", remove_diacritics(text).lower())
