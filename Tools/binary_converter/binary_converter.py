"""
Binary Converter Tool

This module provides functions for converting between binary, decimal, hexadecimal, and ASCII representations.
It also includes a Tkinter-based GUI for interactive conversions.
"""

import tkinter as tk
from tkinter import ttk, messagebox

def binary_to_decimal(digit):
    """
    Convert a binary string to its decimal integer value.

    Args:
        digit (str): Binary string (may contain spaces).

    Returns:
        int or None: Decimal value, or None if input is not valid binary.
    """
    digit = digit.replace(" ", "")
    try:
        for j in digit:
            if j in "10":
                pass
            else:
                return None
        sum = 0
        for i, number in enumerate(digit[::-1]):
            sum += int(number) * 2 ** i
        return sum
    except ValueError:
        pass
     
def decimal_to_binary(digit):
    """
    Convert a decimal integer (as string) to its binary representation (8-bit padded).

    Args:
        digit (str or int): Decimal value.

    Returns:
        str: Binary string, padded to a multiple of 8 bits.
    """
    if int(digit) < 0:
        return None
    try:
        sum = ""
        quotient = int(digit) // 2
        remainder = int(digit) % 2
        sum += str(remainder)
        while True:
            if quotient == 0:
                sum = sum [::-1]
                break
            elif quotient != 0:
                remainder = quotient % 2
                quotient = quotient // 2
                sum += str(remainder)
        while True:
            if len(sum) % 8 == 0:
                return sum
            else:
                sum = "0{}".format(sum)
    except ValueError:
        return None

def hexadecimal_to_decimal(digit):
    """
    Convert a hexadecimal string to its decimal integer value.

    Args:
        digit (str): Hexadecimal string (may contain spaces, case insensitive).

    Returns:
        int: Decimal value.
    """
    digit = digit.replace(" ", "")
    try:
        sum = 0
        hex_original = []
        hex_modified = []
        for i, number in enumerate(str(digit[::-1])):
            hex_original.append(number)
        hex_modified = ["10" if x == "a" or x == "A" else x for x in hex_original]       
        hex_modified = ["11" if x == "b" or x == "B" else x for x in hex_modified]      
        hex_modified = ["12" if x == "c" or x == "C" else x for x in hex_modified]
        hex_modified = ["13" if x == "d" or x == "D" else x for x in hex_modified]
        hex_modified = ["14" if x == "e" or x == "E" else x for x in hex_modified]
        hex_modified = ["15" if x == "f" or x == "F" else x for x in hex_modified]
        for j, number2 in enumerate(hex_modified):
            sum += int(number2) * 16 ** j
        return sum
    except NotImplementedError:
        pass    

def decimal_to_hexadecimal(digit):
    """
    Convert a decimal integer (as string) to its hexadecimal representation.

    Args:
        digit (str or int): Decimal value.

    Returns:
        str: Hexadecimal string.
    """
    if int(digit) < 0:
        return None
    try:
        sum = ""
        quotient = int(digit) // 16
        remainder = int(digit) % 16
        if remainder == 10:
            remainder = "A"
        if remainder == 11:
            remainder = "B"
        if remainder == 12:
            remainder = "C"
        if remainder == 13:
            remainder = "D"
        if remainder == 14:
            remainder = "E"
        if remainder == 15:
            remainder = "F"
        sum += str(remainder)
        while True:
            if quotient == 0:
                sum = sum [::-1]
                return sum
            elif quotient != 0:
                remainder = quotient % 16
                quotient = quotient // 16
                if remainder == 10:
                    remainder = "A"
                if remainder == 11:
                    remainder = "B"
                if remainder == 12:
                    remainder = "C"
                if remainder == 13:
                    remainder = "D"
                if remainder == 14:
                    remainder = "E"
                if remainder == 15:
                    remainder = "F"
                sum += str(remainder)
    except ValueError:
        pass    

def invert_binary(digit):
    """
    Invert a binary string (0s become 1s and vice versa).

    Args:
        digit (str): Binary string.

    Returns:
        str: Inverted binary string.
    """
    digit = digit.replace(" ", "")
    inverse_digit = ""
    for i in digit:
        
        if i == "0":
            inverse_digit += "1"
            
        else:
            inverse_digit += "0"
    return inverse_digit

def binary_to_ascii(digit):
    """
    Convert a binary string to its ASCII text representation.

    Args:
        digit (str): Binary string.

    Returns:
        str: ASCII text.
    """
    digit = digit.replace(" ", "")
    text = ""
    while len(digit) % 8 != 0:
        digit = "0" + digit
    while len(digit) > 0:
        byte = digit[:8]
        digit = digit[8:]
        text += chr(int(byte, 2))
    return text

def ascii_to_binary(text):
    """
    Convert ASCII text to its binary representation (8 bits per character).

    Args:
        text (str): ASCII text.

    Returns:
        str: Binary string, space-separated per byte.
    """
    binary = ""
    for i in text:
        binary += decimal_to_binary(ord(i))
    binary = " ".join(binary[i:i+8] for i in range(0, len(binary), 8))
    return binary


def gui_convert():
    """
    Handle the conversion logic for the GUI, updating the result label and copy button.
    """
    conversion = conversion_var.get()
    input_value = input_entry.get()
    result = ""
    try:
        if conversion == "Binary to Decimal":
            result = binary_to_decimal(input_value)
            result_label.config(text=f"{result}")
        elif conversion == "Decimal to Binary":
            result = decimal_to_binary(input_value)
            result_label.config(text=f"{result}")
        elif conversion == "Hexadecimal to Decimal":
            result = hexadecimal_to_decimal(input_value)
            result_label.config(text=f"{result}")
        elif conversion == "Hexadecimal to Binary":
            dec = hexadecimal_to_decimal(input_value)
            result = decimal_to_binary(dec)
            result_label.config(text=f"{result}")
        elif conversion == "Decimal to Hexadecimal":
            result = decimal_to_hexadecimal(input_value)
            result_label.config(text=f"{result}")
        elif conversion == "Binary to Hexadecimal":
            dec = binary_to_decimal(input_value)
            result = decimal_to_hexadecimal(dec)
            result_label.config(text=f"{result}")
        elif conversion == "Invert Binary":
            result = invert_binary(input_value)
            result_label.config(text=f"{result}")
        elif conversion == "Binary to ASCII":
            result = binary_to_ascii(input_value)
            result_label.config(text=f"{result}")
        elif conversion == "ASCII to Binary":
            result = ascii_to_binary(input_value)
            result_label.config(text=f"{result}")
        else:
            result_label.config(text="Unknown conversion.")
            result = ""
        # Enable copy button if result is not empty
        if result:
            copy_btn.config(state="normal")
        else:
            copy_btn.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {e}")
        copy_btn.config(state="disabled")

def copy_result():
    """
    Copy the current result to the clipboard if available.
    """
    result = result_label.cget("text")
    if result and result != "(output will appear here)" and result != "Unknown conversion.":
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()  # Keeps clipboard after window closes

def main():
    """
    Launch the Tkinter GUI for the binary converter.
    """
    global conversion_var, input_entry, result_label, copy_btn, root
    root = tk.Tk()
    root.title("Binary converter")

    conversions = [
        "Binary to Decimal",
        "Decimal to Binary",
        "Hexadecimal to Decimal",
        "Hexadecimal to Binary",
        "Decimal to Hexadecimal",
        "Binary to Hexadecimal",
        "Invert Binary",
        "Binary to ASCII",
        "ASCII to Binary"
    ]

    frame = ttk.Frame(root, padding=20)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text="Conversion:").grid(row=0, column=0, sticky="w")
    conversion_var = tk.StringVar(value=conversions[0])
    conversion_menu = ttk.Combobox(frame, textvariable=conversion_var, values=conversions, state="readonly", width=25)
    conversion_menu.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Input:").grid(row=1, column=0, sticky="w")
    input_entry = ttk.Entry(frame, width=28)
    input_entry.grid(row=1, column=1, pady=5)

    convert_btn = ttk.Button(frame, text="Convert", command=gui_convert)
    convert_btn.grid(row=2, column=0, columnspan=2, pady=10)

    result_label = ttk.Label(frame, text="(output will appear here)")
    result_label.grid(row=3, column=0, columnspan=2, pady=5)

    copy_btn = ttk.Button(frame, text="Copy output", command=copy_result, state="disabled")
    copy_btn.grid(row=4, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
