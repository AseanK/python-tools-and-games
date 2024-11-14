import tkinter as tk
from tkinter import messagebox
import re
import nltk
from nltk.corpus import words

nltk.download('words')

def check_dictionary(word):
    word_list = set(words.words())
    if word.lower() in word_list:
        return True
    return False

def check_complexity(password):
    if len(password) < 10:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    if re.search(r'(.)\1\1', password):
        return False
    return True

def check_password_strength(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password is too short. Please enter at least 8 characters.")
    if check_dictionary(password):
        feedback.append("Password contains a dictionary word. Use a more complex password.")
    if not check_complexity(password):
        feedback.append("Include uppercase and lowercase letters, numbers, and special characters, and avoid consecutive identical characters.")
    
    if feedback:
        return "\n".join(feedback)
    return "Strong password!"

def on_check_button_click():
    password = entry_password.get()
    result = check_password_strength(password)
    if result == "Strong password!":
        messagebox.showinfo("Strength Check Result", result)
    else:
        messagebox.showwarning("Strength Check Result", result)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

label_password = tk.Label(root, text="Enter Password : ")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

check_button = tk.Button(root, text="Check Password Strength", command=on_check_button_click)
check_button.pack(pady=20)

root.mainloop()