import random
import string
import tkinter as tk
from tkinter import messagebox


# Function to generate a strong password based on a custom word
def generate_password(custom_word):
    # Define the required characters for a strong password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+"

    # Ensure the final password is at least 12 characters
    target_length = max(12, len(custom_word) + 4)

    # Add random selections of characters around the custom word to increase strength
    prefix = [
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    suffix = [
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Combine prefix, custom word, and suffix
    password = ''.join(prefix) + custom_word + ''.join(suffix)

    # Add more random characters if the password is still too short
    while len(password) < target_length:
        password += random.choice(uppercase_letters + lowercase_letters + digits + symbols)

    # Shuffle prefix and suffix slightly to add randomness
    password_list = list(password)
    random.shuffle(password_list[:len(prefix)])
    random.shuffle(password_list[-len(suffix):])
    final_password = ''.join(password_list)

    return final_password


# Function to display generated password
def display_password():
    custom_word = entry.get()
    if not custom_word:
        messagebox.showerror("Error", "Please enter a custom word")
        return

    password = generate_password(custom_word)
    result_label.config(text="Generated Password: " + password)
    copy_button.config(state="normal")  # Enable copy button
    result_label.password = password  # Store password for copying


# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# Setting up the UI
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

# Input label and entry box
label = tk.Label(root, text="Enter a custom word:")
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=display_password)
generate_button.pack(pady=10)

# Result label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Copy button to copy password to clipboard
copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard, state="disabled")
copy_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
