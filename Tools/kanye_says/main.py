import requests
import tkinter as tk

# Fetch API and display
def get_quote():
    res = requests.get(url="https://api.kanye.rest")
    res.raise_for_status()
    data = res.json()
    canvas.itemconfig(quote_text, text=data["quote"])


# Window GUI
window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
window.resizable(width=False, height=False)

canvas = tk.Canvas(width=300, height=414)
bg_img = tk.PhotoImage(file="background.png")
canvas.create_image(150,207, image=bg_img)
quote_text = canvas.create_text(150, 207, text="Click me!", width=250, font=("Arial", 18, "bold"))
canvas.grid(row=0,column=0)

btn_img = tk.PhotoImage(file="kanye.png")
btn = tk.Button(image=btn_img, highlightthickness=0, command=get_quote)
btn.config(bd=0)
btn.grid(row=1, column=0)

window.mainloop()