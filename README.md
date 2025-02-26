# Simple Cryptography application using Command-Line Interface with `argparse`
## Description
This application was built only for the purpose of playing around with [`argparse`](https://realpython.com/command-line-interfaces-python-argparse/) module of Python. It includes 3 different cryptography method to encrypt or decrypt a message with a given key, including Caesar Cipher, Substitution Cipher, and Speak-to-Three.
## User's guide
For displaying guide in terminal, type:
```sh
iscrypt -h
```
For more details on each subcommand, type:
```sh
iscrypt <subcommand-name> -h
```
General command:
```sh
iscypt <subcommand-name> <option> <key> <message>
```
### Subcommands:
- `caesar`: encode/decode with Caesar Cipher
- `sub`: encode/decode with Substitution Cipher
- `speak-to-3`: encode with speak-to-three, note that this method never includes decoding
### Required flags & arguments:
- `caesar [-e / --encode] <key> <message>`: Encode with Caesar Cipher with key and message
- `caesar [-d / --decode] <key> <message>`: Decode with Caesar Cipher with key and message
- `sub [-e / --encode] <key> <message>`: Encode with Substitution Cipher with key and message. Key is a string of 26 unique alphabetical letters
- `sub [-e / --encode] <key> <message>`: Decode with Substitution Cipher with key and message. Key is a string of 26 unique alphabetical letters
- `speak-to-3 <message>`: Encode with Speak-to-three. There is no option for decoding.
## Installation
For obtaining the repository, type:
```sh
git clone https://github.com/dinhphucdat/Crypt
```
Then, navigate into the repository:
```sh
cd ./script_app
```
System set-up:
```sh
pip install .
```
After which you are good to go! Have a nice time using the tool!
