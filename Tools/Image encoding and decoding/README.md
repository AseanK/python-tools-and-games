# Image Encoder and Decoder

A Python program that enables users to encode images into Base64 text for easy sharing across text-based platforms and decode the text back into the original image files. This tool is designed to simplify image sharing and recovery without relying on binary file transfers.

---

## Features

- **Image Encoding**: Converts images into Base64-encoded text files, making them suitable for embedding in text documents or sharing via chat and email.
- **Text-to-Image Decoding**: Restores the original image from Base64-encoded text files.
- **File Navigation**: Allows users to navigate directories and manage file selection via a command-line interface.
- **Automated File Naming**: Automatically saves encoded and decoded files with descriptive names to prevent overwriting and enhance organization.

---

## Requirements

- **Python 3.6+**

This program uses only built-in Python modules (`os` and `base64`), so no additional dependencies are needed.

---

## How It Works

### Encoding Process
1. Reads the image file in binary mode.
2. Converts the binary data into a Base64-encoded string.
3. Saves the string into a text file with a user-friendly name.

### Decoding Process
1. Reads the Base64 string from a text file.
2. Decodes the string back into binary image data.
3. Writes the binary data into an image file.

---

## Customization

- **File Naming**: Modify the naming conventions for encoded or decoded files in the `encode_image` and `decode_image` functions.
- **Batch Processing**: Extend the program to handle multiple files simultaneously for encoding or decoding.
- **Character Limit Handling**: Add functionality to split encoded text into chunks for platforms with character limits.

---

## Troubleshooting

### Common Issues
- **File Not Found**: Ensure the file exists in the current directory and the name is entered correctly.
- **Decoding Errors**: Ensure the Base64 text is unaltered before decoding.
- **Invalid Directories**: Verify that directory names exist when navigating.

### Tips
- Use complete file names, including extensions, when selecting files.
- Avoid manually modifying encoded text files to prevent decoding errors.

---

## Notes

### Use Cases
- **Portable Image Sharing**: Share images via text-based platforms like emails, chat, or forums without relying on attachments.
- **Embedding Visuals in Code**: Include images as Base64 text in configuration files or scripts for portability.
- **Cross-Platform Support**: The program works on all operating systems that support Python 3.6 or later.

### Known Limitations
- Base64-encoded text files are larger than the original images due to encoding overhead.
- Processing very large images may require significant memory.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the Python community for documentation and resources.
- This project was inspired by the need for seamless image sharing and recovery in text-based environments.
