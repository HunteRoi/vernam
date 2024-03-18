"""Module providing the feature to encrypt text."""

from src.vernam_cipher import vernam_cipher


def encrypt(plaintext: str, key: str) -> bytes:
    """Encrypt text."""
    return vernam_cipher(plaintext, key)
