<p align="center">
  <a href="https://github.com/AseanK/python-tools-and-games" target="_blank">
    <img src="../../images/tools_logo.png" width = "2560px" height = "200px">
  </a>
</p>

# Encrypt and Decrypt Tool
<!-- Tools features -->
## Features
1. Encrypt long text directly from the command line.
2. Decrypt encrypted strings back to plain text.
3. Encrypt entire files, like documents or images.
4. Generates a secure, cryptographically strong key for safe AES-128 encryption (via Fernet).

## How to install and run
1. Fork the repo by clicking the fork logo on the top right <img src="../../images/fork.png" width="300" height="60">
2. Clone the repo `git clone git@github.com:AseanK/python-tools-and-games.git`
3. Head to the `Tools/encrypt_decrypt_tool` folder
4. Install the requirements using `pip install -r requirements.txt`
5. Generate a new key by running: `python encrypt_decrypt.py keygen`
6. Encrypt text: `python encrypt_decrypt.py encrypt --key YOUR_KEY --text "my secret"`
7. Decrypt text: `python encrypt_decrypt.py decrypt --key YOUR_KEY --text "encrypted_string"`
8. Encrypt a file: `python encrypt_decrypt.py encrypt --key YOUR_KEY --file document.pdf`
9. Run `python encrypt_decrypt.py -h` to see all available commands.
