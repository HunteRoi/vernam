"""Vernam cipher module."""

def vernam_cipher(text: str | bytes, key: str) -> bytes:
    """Apply the Vernam cipher to encrypt or decrypt the input text."""
    if not text:
        raise ValueError('Input is empty.')
    if not key:
        raise ValueError('Key is empty.')

    if len(key) < len(text):
        key = (key * (len(text) // len(key) + 1))[:len(text)]

    key_bytes: bytes = key.encode()
    text_bytes: bytes = text.encode() if isinstance(text, str) else text

    return bytes(p ^ k for p, k in zip(text_bytes, key_bytes))
