import argparse
import sys
import os

try:
    from cryptography.fernet import Fernet
except ImportError:
    print("Please install the 'cryptography' library. Run: pip install -r requirements.txt")
    sys.exit(1)

def generate_key():
    key = Fernet.generate_key()
    print(f"Generated Key: {key.decode('utf-8')}")
    print("Please save this key in a secure location. You will need it to decrypt your data.")

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data)

def decrypt_data(data, key):
    f = Fernet(key)
    return f.decrypt(data)

def main():
    parser = argparse.ArgumentParser(description="Encrypt and decrypt text using symmetric encryption.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: keygen
    parser_keygen = subparsers.add_parser("keygen", help="Generate a new encryption key")

    # Command: encrypt
    parser_encrypt = subparsers.add_parser("encrypt", help="Encrypt text")
    parser_encrypt.add_argument("-k", "--key", required=True, help="Encryption key (base64 encoded)")
    parser_encrypt.add_argument("-t", "--text", required=True, help="Text to encrypt")

    # Command: decrypt
    parser_decrypt = subparsers.add_parser("decrypt", help="Decrypt text")
    parser_decrypt.add_argument("-k", "--key", required=True, help="Decryption key (base64 encoded)")
    parser_decrypt.add_argument("-t", "--text", required=True, help="Text to decrypt")

    args = parser.parse_args()

    if args.command == "keygen":
        generate_key()
    
    elif args.command == "encrypt":
        try:
            key = args.key.encode('utf-8')
            encrypted = encrypt_data(args.text.encode('utf-8'), key)
            print(f"Encrypted text: {encrypted.decode('utf-8')}")
        except Exception as e:
            print(f"Encryption failed: {e}")

    elif args.command == "decrypt":
        try:
            key = args.key.encode('utf-8')
            decrypted = decrypt_data(args.text.encode('utf-8'), key)
            print(f"Decrypted text: {decrypted.decode('utf-8')}")
        except Exception as e:
            print(f"Decryption failed: {e}")
            print("Make sure you are using the correct key and valid encrypted data.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
