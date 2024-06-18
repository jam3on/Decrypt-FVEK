# Decrypt-FVEK

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.MIT)
[![Language: Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![x64](https://img.shields.io/badge/Windows-64_bit-0078d7.svg)](#)
[![v1.0](https://img.shields.io/badge/Version-1.0-ff5733.svg)](#)

Decrypt-FVEK is a software tool designed to decrypt an FVEK (Full Volume Encryption Key) from a BitLocker-encrypted computer using the VMK (Volume Master Key) stored in the TPM (Trusted Platform Module), a nonce, a MAC (Message Authentication Code), and an encrypted key from a hard drive.

## Installation

First, install the required Python packages. You can do this by running the following command:

```sh
pip install -r requirements.txt
```

## Usage

To use this tool from the command line, run the following command:

```sh
fvek.py -vmk vmk -nonce nonce -mac mac -key encrypted_key
```

Replace `vmk`, `nonce`, `mac`, and `encrypted_key` with the appropriate values.

## Creating an Executable Binary

To create an executable binary, you will need to install `pyinstaller`. You can install it using pip:

```sh
pip install pyinstaller
```

After installing `pyinstaller`, you can create the executable using the following command:

```sh
pyinstaller --icon=icon.ico --onefile --windowed .\fvek.py
```

This command will generate a standalone executable file for Decrypt-FVEK.