"""Module providing the feature to encrypt text."""

from src.infrastructure.cipher_service import vernam_cipher


def encrypt(plaintext: str, key: str) -> bytes:
    """Encrypt plaintext."""
    return vernam_cipher(plaintext, key)
