"""Module providing the feature to decrypt text."""

from src.vernam_cipher import vernam_cipher


def decrypt(ciphertext: bytes, key: str) -> str:
    """Decrypt text."""
    return vernam_cipher(ciphertext, key).decode()
