# SDA 2023-2024
MASI course asset "Sécurité des Applications".
Topic on frequency analysis.

## Getting started

Install the requirements with the follwoing commands:
```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Running the CLI

As stated in the documentation, the CLI has several options.
You can visualize them by running the CLI with the following command :
```bash
$ python vernam.py -h
```

Several commands are available, with their batch of options. **Please carefully read the docs before using.**

⚠️ In regard to the instructions of this exercise, a slight difference is to be noted. The parameters `--encrypt` and `--decrypt` are __not__ parameters in this version of the program.
Wich means you should use them with the `--` !

### Encrypt

The used command to validate the encryption feature is `python vernam.py encrypt --in ./resources/input/plain.txt --out ./resources/output/cipher.txt --key mykey`.

### Decrypt

The used command to validate the decryption feature is `python vernam.py decrypt --in ./resources/input/cipher.txt --out ./resources/output/plain.txt --key mykey`.

### Attack

The used command to validate the attack feature is `python vernam.py attack --in ./resources/input/attack_cipher.txt --out ./resources/output/attack_plain.txt`.

## Contributors

[etu45363 - ARTS Loïck](https://gitlab.com/ArtsLoick45363)
[etu33784 - DEVRESSE Tinaël](https://gitlab.com/hunteroi)
