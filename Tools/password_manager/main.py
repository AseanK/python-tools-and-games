import tkinter as tk
from tkinter import messagebox
import random

# Global val
CHARCOAL = "#303437"
RED = "#d73e3e"


# Fetch data from data.txt and display saved websites
def get_saved():
    with open("data.txt") as data:
        web = data.readlines()
    
    for i in web:
        result = i.split(" | ")[1]
        web_list.insert(tk.END, f"{result}\n", "tag-center")


# Generate random password
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    new_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    new_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = new_letters + new_numbers + new_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)


# Save user's input data to data.txt
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website != "" and email != "" and password != "":
        with open("data.txt", mode="a") as data:
            data.write(f"{website} | {email} | {password} \n")
        web_entry.delete(0, "end")
        email_entry.delete(0, "end")
        password_entry.delete(0, "end")
        web_list.insert(tk.END, f"{website}\n", "tag-center")
        messagebox.showinfo(title="Success", message="Successfully saved")
    else:
        messagebox.showerror(title="Failed", message="Please fill out the boxes")


# GUI
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=CHARCOAL)

canvas = tk.Canvas(width=280, height=200, highlightthickness=0, bg=CHARCOAL)
img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)

website_label = tk.Label(text="Website:")
website_label.config(bg=CHARCOAL, fg="white")

email_label = tk.Label(text="Email/Username:")
email_label.config(bg=CHARCOAL, fg="white")

password_label = tk.Label(text="Password:")
password_label.config(bg=CHARCOAL, fg="white")

web_entry = tk.Entry(width=35)
web_entry.focus()

email_entry = tk.Entry(width=35)

password_entry = tk.Entry(width=28)

gen_btn = tk.Button(text="Generate", command=generate)
gen_btn.config(bg=RED, activebackground=RED)

add_btn = tk.Button(text="Add", command=save)
add_btn.config(bg=RED, activebackground=RED)

web_list = tk.Text(
    width=22,
    height=18,
    bg=CHARCOAL,
    fg="white",
    highlightthickness=0
)
web_list.tag_configure('tag-center', justify='center')
web_list.bind("<Key>", lambda e: "break")
get_saved()

# GUI Grid
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
web_entry.grid(column=1, row=1, columnspan=2, sticky="W")
email_entry.grid(column=1, row=2, columnspan=2, sticky="W")
password_entry.grid(column=1, row=3, sticky="W")
gen_btn.grid(column=1,row=3, padx= 175)
add_btn.grid(column=1, row=4, ipadx=100, sticky="W")
web_list.grid(column=1, row=0, rowspan=5, sticky="E")

window.mainloop()