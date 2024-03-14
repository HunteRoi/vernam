"""Module providing CLI to (en/de)crypt and attack files using the Vernam cipher."""

import sys
import click

from src.preprocess import sanitize_to_alpha


@click.group()
def cli():
    """
    Example script to read and write file/stdin while sanitizing the input.
    """


@cli.command()
@click.option(
    '--output-newlines/--ignore-newlines', default=True, show_default=True,
    help=('Whether to output or ignore new lines as in the input.')
)
@click.option(
    '--output', 'output_file', type=click.File('w'), default=sys.stdout,
    help="Output file path. Use - to output on stdout. [default: stdout]"
)
@click.argument('input_file', nargs=1, type=click.File('r'), default=sys.stdin)
def sanitize(output_newlines, output_file, input_file):
    """
    Sanitize text.

    Read the text from INPUT_FILE. Use - to read from stdin.
    """
    if output_newlines:
        def write(line):
            print(line, file=output_file)
    else:
        def write(line):
            output_file.write(line)

    for line in input_file:
        write(sanitize_to_alpha(line))


if __name__ == '__main__':
    cli()
