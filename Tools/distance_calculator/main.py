import tkinter as tk

window = tk.Tk()
window.title("Distance conversion calculator")
window.config(padx=40,pady=40, background="dark gray")


def convert():
    miles_to_km()
    miles_to_ft()
    miles_to_yd()
    miles_to_m()


def miles_to_km():
    miles = float(inp.get())
    km = round(miles * 1.609)
    result_km.config(text=f"{km} km")

def miles_to_m():
    miles = float(inp.get())
    m = round(miles * 1609)
    result_m.config(text=f"{m} m")

def miles_to_ft():
    miles = float(inp.get())
    ft = round(miles * 5280)
    result_ft.config(text=f"{ft} ft")

def miles_to_yd():
    miles = float(inp.get())
    yd = round(miles * 1760)
    result_yd.config(text=f"{yd} yd")


start_label = tk.Label(text="Enter distance in mile")
start_label.grid(row=0, column=2)
start_label.config(pady=15, font=("Arial", 12), background="dark gray")

inp = tk.Entry()
inp.grid(row=1, column=2)
inp.insert(tk.END, string="0")

result_km = tk.Label(text="0 km")
result_km.grid(row=2, column=0)
result_km.config(padx=15, font=("Arial", 10))

result_m = tk.Label(text="0 m")
result_m.grid(row=2, column=1)
result_m.config(padx=15, font=("Arial", 10))

result_ft = tk.Label(text="0 ft")
result_ft.grid(row=2, column=3)
result_ft.config(padx=15, font=("Arial", 10))

result_yd = tk.Label(text="0 yd")
result_yd.grid(row=2, column=4)
result_yd.config(padx=15, font=("Arial", 10))

button = tk.Button(text="Calculate", command=convert)
button.grid(row=3, column=2)
button.config(borderwidth=2, font=("Arial", 12))


window.mainloop()