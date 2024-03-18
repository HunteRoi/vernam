"""Module providing CLI to (en/de)crypt and attack files using the Vernam cipher."""

import sys
import click
from click import File

from src.preprocess import sanitize_to_alpha
from src.encrypt import encrypt
from src.decrypt import decrypt
from src.attack import attack

@click.group()
def cli():
    """
    CLI to (en/de)crypt and attack files using the Vernam cipher.
    """

@cli.command('encrypt')
@click.option(
    '--in', 'input_file',
    type=File('r'), default=sys.stdin, required=True,
    help='Input file path. Use - to read from stdin. [default: stdin]'
)
@click.option(
    '--out', 'output_file',
    type=File('wb'), default=sys.stdout, required=True,
    help='Output file path. Use - to output on stdout. [default: stdout]'
)
@click.option(
    '--key', 'key',
    type=str, default=None, required=True,
    help='Key to use for encryption/decryption.'
)
def encrypt_command(input_file: File, output_file: File, key: str):
    """Encrypt text."""
    input_text = input_file.read()
    output_file.write(encrypt(sanitize_to_alpha(input_text), key))

@cli.command('decrypt')
@click.option(
    '--in', 'input_file',
    type=File('rb'), default=sys.stdin, required=True,
    help='Input file path. Use - to read from stdin. [default: stdin]'
)
@click.option(
    '--out', 'output_file',
    type=File('w'), default=sys.stdout, required=True,
    help='Output file path. Use - to output on stdout. [default: stdout]'
)
@click.option(
    '--key', 'key',
    type=str, default=None, required=True,
    help='Key to use for encryption/decryption.'
)
def decrypt_command(input_file: File, output_file: File, key: str):
    """Decrypt text."""
    cipher_text = input_file.read()
    output_file.write(decrypt(cipher_text, key))

@cli.command('attack')
@click.option(
    '--in', 'input_file',
    type=File('r'), default=sys.stdin, required=True,
    help='Input file path. Use - to read from stdin. [default: stdin]'
)
@click.option(
    '--out', 'output_file',
    type=File('w'), default=sys.stdout, required=True,
    help='Output file path. Use - to output on stdout. [default: stdout]'
)
def attack_command(input_file: File, output_file: File):
    """Attack text."""
    attack()


if __name__ == '__main__':
    cli()
