"""Module providing CLI to (en/de)crypt and attack files using the Vernam cipher."""

import sys
import click

from src.preprocess import sanitize
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
    type=click.File('r'), default=sys.stdin, required=True,
    help='Input file path. Use - to read from stdin. [default: stdin]'
)
@click.option(
    '--out', 'output_file',
    type=click.File('w'), default=sys.stdout, required=True,
    help='Output file path. Use - to output on stdout. [default: stdout]'
)
@click.option(
    '--key', 'key',
    type=str, default=None, required=True,
    help='Key to use for encryption/decryption.'
)
def encrypt_command(input_file, output_file, key):
    """Encrypt text."""
    encrypt()

@cli.command('decrypt')
@click.option(
    '--in', 'input_file',
    type=click.File('r'), default=sys.stdin, required=True,
    help='Input file path. Use - to read from stdin. [default: stdin]'
)
@click.option(
    '--out', 'output_file',
    type=click.File('w'), default=sys.stdout, required=True,
    help='Output file path. Use - to output on stdout. [default: stdout]'
)
@click.option(
    '--key', 'key',
    type=str, default=None, required=True,
    help='Key to use for encryption/decryption.'
)
def decrypt_command(input_file, output_file, key):
    """Decrypt text."""
    decrypt()

@cli.command('attack')
@click.option(
    '--in', 'input_file',
    type=click.File('r'), default=sys.stdin, required=True,
    help='Input file path. Use - to read from stdin. [default: stdin]'
)
@click.option(
    '--out', 'output_file',
    type=click.File('w'), default=sys.stdout, required=True,
    help='Output file path. Use - to output on stdout. [default: stdout]'
)
def attack_command(input_file, output_file):
    """Attack text."""
    attack()


if __name__ == '__main__':
    cli()
