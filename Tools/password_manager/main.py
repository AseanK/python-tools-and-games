import tkinter as tk

CHARCOAL = "#303437"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# GUI
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=CHARCOAL)


canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bg=CHARCOAL)
img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)

canvas.grid(row=1, column=1)

window.mainloop()