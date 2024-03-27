"""Module providing CLI to (en/de)crypt and attack files using the Vernam cipher."""

import sys
import click

from src.application.preprocess import sanitize_to_alpha
from src.application.commands.encrypt import encrypt
from src.application.commands.decrypt import decrypt
from src.application.commands.attack import attack


@click.group()
def cli():
    """
    CLI to (en/de)crypt and attack files using the Vernam cipher.
    """


@cli.command("encrypt")
@click.option(
    "--in",
    "input_file",
    type=click.File("r"),
    default=sys.stdin,
    required=True,
    help="Input file path. Use - to read from stdin. [default: stdin]",
)
@click.option(
    "--out",
    "output_file",
    type=click.File("wb"),
    default=sys.stdout,
    required=True,
    help="Output file path. Use - to output on stdout. [default: stdout]",
)
@click.option(
    "--key",
    "key",
    type=str,
    default=None,
    required=True,
    help="Key to use for encryption/decryption.",
)
def encrypt_command(input_file: click.File, output_file: click.File, key: str):
    """Encrypt text."""
    input_text = input_file.read()
    output_file.write(encrypt(sanitize_to_alpha(input_text), key))


@cli.command("decrypt")
@click.option(
    "--in",
    "input_file",
    type=click.File("rb"),
    default=sys.stdin,
    required=True,
    help="Input file path. Use - to read from stdin. [default: stdin]",
)
@click.option(
    "--out",
    "output_file",
    type=click.File("w"),
    default=sys.stdout,
    required=True,
    help="Output file path. Use - to output on stdout. [default: stdout]",
)
@click.option(
    "--key",
    "key",
    type=str,
    default=None,
    required=True,
    help="Key to use for encryption/decryption.",
)
def decrypt_command(input_file: click.File, output_file: click.File, key: str):
    """Decrypt text."""
    cipher_text = input_file.read()
    output_file.write(decrypt(cipher_text, key))


@cli.command("attack")
@click.option(
    "--in",
    "input_file",
    type=click.File("rb"),
    default=sys.stdin,
    required=True,
    help="Input file path. Use - to read from stdin. [default: stdin]",
)
@click.option(
    "--out",
    "output_file",
    type=click.File("w"),
    default=sys.stdout,
    required=True,
    help="Output file path. Use - to output on stdout. [default: stdout]",
)
@click.option(
    "--silent",
    "silent",
    type=bool,
    default=False,
    required=False,
    is_flag=True,
    help="Silence the output.",
)
def attack_command(input_file: click.File, output_file: click.File, silent: bool):
    """Attack text."""
    cipher_text = input_file.read()
    output_file.write(
        attack(cipher_text, click.echo if not silent else lambda *args, **kwargs: None)
    )


if __name__ == "__main__":
    cli()
