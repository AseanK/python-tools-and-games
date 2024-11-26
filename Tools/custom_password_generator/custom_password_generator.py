import random
import string
import tkinter as tk
from tkinter import messagebox
from typing import Optional


# Function to generate a strong password based on a custom word
def generate_password(custom_word: str) -> str:
    # Define the required characters for a strong password
    uppercase_letters: str = string.ascii_uppercase
    lowercase_letters: str = string.ascii_lowercase
    digits: str = string.digits
    symbols: str = "!@#$%^&*()-_=+"

    # Ensure the final password is at least 12 characters
    target_length: int = max(12, len(custom_word) + 4)

    # Add random selections of characters around the custom word to increase strength
    prefix: list[str] = [
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    suffix: list[str] = [
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Combine prefix, custom word, and suffix
    password: str = ''.join(prefix) + custom_word + ''.join(suffix)

    # Add more random characters if the password is still too short
    while len(password) < target_length:
        password += random.choice(uppercase_letters + lowercase_letters + digits + symbols)

    # Shuffle prefix and suffix slightly to add randomness
    password_list: list[str] = list(password)
    random.shuffle(password_list[:len(prefix)])
    random.shuffle(password_list[-len(suffix):])
    final_password: str = ''.join(password_list)

    return final_password


# Function to display generated password
def display_password() -> None:
    custom_word: str = entry.get()
    if not custom_word:
        messagebox.showerror("Error", "Please enter a custom word")
        return

    password: str = generate_password(custom_word)
    result_label.config(text="Generated Password: " + password)
    copy_button.config(state="normal")  # Enable copy button
    result_label.password = password  # Store password for copying


# Function to copy password to clipboard
def copy_to_clipboard() -> None:
    if result_label.password is not None:
        root.clipboard_clear()
        root.clipboard_append(result_label.password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy")


# Setting up the UI
root: tk.Tk = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

# Input label and entry box
label: tk.Label = tk.Label(root, text="Enter a custom word:")
label.pack(pady=10)

entry: tk.Entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Generate button
generate_button: tk.Button = tk.Button(root, text="Generate Password", command=display_password)
generate_button.pack(pady=10)

# Result label to display the generated password
result_label: tk.Label = tk.Label(root, text="")
result_label.pack(pady=10)
result_label.password: Optional[str] = None  # Store password as an optional attribute

# Copy button to copy password to clipboard
copy_button: tk.Button = tk.Button(root, text="Copy Password", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
