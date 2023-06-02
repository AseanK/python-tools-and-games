import tkinter as tk
from time import sleep
import math

# Global val
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# Reset timer
def reset():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(time, text="00:00")
    start_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    check_mark.config(text="")
    reps = 0


# Pass correct time to the count_down function
def start_timer():
    global reps
    reps += 1

    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        start_label.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        start_label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        count_down(WORK_MIN * 60)
        start_label.config(text="Work", fg=GREEN, bg=YELLOW)


# Count down
def count_down(count):
    global timer

    min = math.floor(count / 60)
    sec = count % 60
    
    # Better display
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(time, text=f"{min}:{sec}")

    if count > 0:
        timer = window.after(1, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += " ✔ "
        check_mark.config(text=mark)
        if reps > 8:
            reset()
        

# GUI
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=60, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
time = canvas.create_text(100,135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_label = tk.Label(text="Timer")
start_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))

start_btn = tk.Button(text="Start", command=start_timer)
start_btn.config(bg=GREEN, font=(FONT_NAME, 12))

reset_btn = tk.Button(text="Reset", command=reset)
reset_btn.config(bg=GREEN, font=(FONT_NAME, 12))

check_mark = tk.Label()
check_mark.config(fg=RED, bg=YELLOW, font=(FONT_NAME, 8))

# GUi grid
start_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)
check_mark.grid(row=3, column=1)

window.mainloop()