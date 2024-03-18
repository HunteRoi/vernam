"""Vernam cipher module."""

def vernam_cipher(text: str | bytes, key: str) -> bytes:
    """Encrypt/Decrypt text using the Vernam cipher."""
    if not text:
        raise ValueError('Input is empty.')
    if not key:
        raise ValueError('Key is empty.')

    if len(key) < len(text):
        key = (key * (len(text) // len(key) + 1))[:len(text)]

    if isinstance(text, str):
        return bytes(ord(c) ^ ord(k) for c, k in zip(text, key))

    return bytes(c ^ ord(k) for c, k in zip(text, key))
