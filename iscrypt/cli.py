import argparse
from . import *


def add_wrapper_caesar(args):
    caesarClient(args.encode, args.key, args.message)

def add_wrapper_sub(args):
    substitutionClient(args.encode, args.key, args.message)

def add_wrapper_speak(args):
    speakToThreeClient(args.message)

def main():
    parser = argparse.ArgumentParser(
        prog="iscrypt", 
        description="Enscrypt/Descrypt your message", 
        epilog="Thanks for using %(prog)s! :)"
        )

    subparser = parser.add_subparsers(title="subcommands", help="cryptography choice operation")

    caesar_parser = subparser.add_parser("caesar", help="encode/decode with Caesar Cipher")
    caesar_group = caesar_parser.add_mutually_exclusive_group(required=True)
    caesar_group.add_argument("-e", "--encode", action="store_true")
    caesar_group.add_argument("-d", "--decode", action="store_true")
    caesar_parser.add_argument("key", type=int, help="Shifting distance for all letters in the message")
    caesar_parser.add_argument("message", type=str, help="Message to encode/decode")
    caesar_parser.set_defaults(func=add_wrapper_caesar)

    substitution_parser = subparser.add_parser("sub", help="encode/decode with Substitution Cipher")
    substitution_group = substitution_parser.add_mutually_exclusive_group(required=True)
    substitution_group.add_argument("-e", "--encode", action="store_true")
    substitution_group.add_argument("-d", "--decode", action="store_true")
    substitution_parser.add_argument("key", type=str, help="26-letter key with each letter unique in the alphabet")
    substitution_parser.add_argument("message", type=str, help="Message to encode/decode")
    substitution_parser.set_defaults(func=add_wrapper_sub)

    speak33_parser = subparser.add_parser("speak-to-3", help="encode with speak-to-three, note that this method never includes decoding")
    speak33_parser.add_argument("message", type=str, help="Message to encode")
    speak33_parser.set_defaults(func=add_wrapper_speak)

    # Parse and execute
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
