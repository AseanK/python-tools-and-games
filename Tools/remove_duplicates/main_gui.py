import tkinter as tk
from tkinter import filedialog, messagebox
from main import remove_duplicates
import os


def select_input_file():
    input_file = filedialog.askopenfilename(
        title="Select Input File",
        filetypes=[("Supported Files", "*.txt *.csv *.json *.xlsx *.xml")]
    )
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file)


def process_file():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()

    if not input_file:
        messagebox.showerror("Input Error", "Please select an input file.")
        return

    # 기본 출력 파일 이름 설정
    if not output_file:
        file_ext = os.path.splitext(input_file)[1]
        default_output = f"{os.path.splitext(input_file)[0]}_output{file_ext}"
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, default_output)
        output_file = default_output

    try:
        remove_duplicates(input_file, output_file)
        messagebox.showinfo("Success", f"Duplicates removed and saved to {output_file}.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# GUI Setup
root = tk.Tk()
root.title("Duplicate Remover")

# Input File Selection
tk.Label(root, text="Input File:").grid(row=0, column=0, padx=5, pady=5)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Output File Input
tk.Label(root, text="Output File:").grid(row=1, column=0, padx=5, pady=5)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)

# Process Button
tk.Button(root, text="Remove Duplicates", command=process_file, bg="blue", fg="white").grid(
    row=2, column=1, pady=20)

root.mainloop()
