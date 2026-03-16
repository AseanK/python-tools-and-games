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
    parser = argparse.ArgumentParser(description="Encrypt and decrypt files or text using symmetric encryption.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: keygen
    parser_keygen = subparsers.add_parser("keygen", help="Generate a new encryption key")

    # Command: encrypt
    parser_encrypt = subparsers.add_parser("encrypt", help="Encrypt a file or text")
    parser_encrypt.add_argument("-k", "--key", required=True, help="Encryption key (base64 encoded)")
    group_enc = parser_encrypt.add_mutually_exclusive_group(required=True)
    group_enc.add_argument("-t", "--text", help="Text to encrypt")
    group_enc.add_argument("-f", "--file", help="File to encrypt")
    parser_encrypt.add_argument("-o", "--out", help="Output file to save the encrypted data (optional)")

    # Command: decrypt
    parser_decrypt = subparsers.add_parser("decrypt", help="Decrypt a file or text")
    parser_decrypt.add_argument("-k", "--key", required=True, help="Decryption key (base64 encoded)")
    group_dec = parser_decrypt.add_mutually_exclusive_group(required=True)
    group_dec.add_argument("-t", "--text", help="Text to decrypt")
    group_dec.add_argument("-f", "--file", help="File to decrypt")
    parser_decrypt.add_argument("-o", "--out", help="Output file to save the decrypted data (optional)")

    args = parser.parse_args()

    if args.command == "keygen":
        generate_key()
    
    elif args.command == "encrypt":
        try:
            key = args.key.encode('utf-8')
            if args.text:
                encrypted = encrypt_data(args.text.encode('utf-8'), key)
                if args.out:
                    with open(args.out, 'wb') as f:
                        f.write(encrypted)
                    print(f"Encrypted text saved to: {args.out}")
                else:
                    print(f"Encrypted text: {encrypted.decode('utf-8')}")
            
            elif args.file:
                if not os.path.isfile(args.file):
                    print(f"Error: File '{args.file}' not found.")
                    sys.exit(1)
                with open(args.file, 'rb') as f:
                    data = f.read()
                encrypted = encrypt_data(data, key)
                
                out_file = args.out if args.out else args.file + ".enc"
                with open(out_file, 'wb') as f:
                    f.write(encrypted)
                print(f"Encrypted file saved to: {out_file}")
                
        except Exception as e:
            print(f"Encryption failed: {e}")

    elif args.command == "decrypt":
        try:
            key = args.key.encode('utf-8')
            if args.text:
                decrypted = decrypt_data(args.text.encode('utf-8'), key)
                if args.out:
                    with open(args.out, 'wb') as f:
                        f.write(decrypted)
                    print(f"Decrypted text saved to: {args.out}")
                else:
                    try:
                        print(f"Decrypted text: {decrypted.decode('utf-8')}")
                    except UnicodeDecodeError:
                        print(f"Decrypted data is not valid UTF-8. Please save to a file using -o/--out.")
            
            elif args.file:
                if not os.path.isfile(args.file):
                    print(f"Error: File '{args.file}' not found.")
                    sys.exit(1)
                with open(args.file, 'rb') as f:
                    data = f.read()
                decrypted = decrypt_data(data, key)
                
                out_file = args.out
                if not out_file:
                    if args.file.endswith(".enc"):
                        out_file = args.file[:-4]
                    else:
                        out_file = args.file + ".dec"
                        
                with open(out_file, 'wb') as f:
                    f.write(decrypted)
                print(f"Decrypted file saved to: {out_file}")
                
        except Exception as e:
            print(f"Decryption failed: {e}")
            print("Make sure you are using the correct key and valid encrypted data.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
