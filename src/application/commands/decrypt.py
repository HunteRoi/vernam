"""Module providing the feature to decrypt text."""

from src.infrastructure.cipher_service import vernam_cipher


def decrypt(ciphertext: bytes, key: str) -> str:
    """Decrypt ciphertext."""
    return vernam_cipher(ciphertext, key).decode()
