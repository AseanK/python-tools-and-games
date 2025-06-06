import tkinter as tk
from time import sleep
import math

# Global val
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdead"
YELLOW = "#f8e2aa"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# Raise window in after each cycle
def raise_above_all(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


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

    if reps > 1:
        window.after_cancel(timer)

    if reps % 8 == 0:
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
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        raise_above_all(window)

        for _ in range(math.floor(reps / 2)):
            mark += " ✔ "
        check_mark.config(text=mark)
        if reps > 8:
            reset()
        

# Add tasks to list_box
def new_task():
    task = todo_entry.get()

    if task != "":
        list_box.insert(tk.END, task)
        todo_entry.delete(0, "end")


# Delete tasks from list_box
def del_task():
    list_box.delete(tk.ANCHOR)


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
start_btn.config(bg=GREEN, font=(FONT_NAME, 12), activebackground=GREEN)

reset_btn = tk.Button(text="Reset", command=reset)
reset_btn.config(bg=GREEN, font=(FONT_NAME, 12), activebackground=GREEN)

check_mark = tk.Label()
check_mark.config(fg=RED, bg=YELLOW, font=(FONT_NAME, 8))

todo_label = tk.Label(text="Tasks", font=(FONT_NAME, 16, "bold"))
todo_label.config(bg=YELLOW, fg=PINK)

list_box = tk.Listbox(
    width=25,
    height=8,
    font=(FONT_NAME, 12),
    bg=YELLOW,
    highlightthickness=0,
    selectbackground=PINK,
    activestyle="none"
)

todo_entry = tk.Entry(font=(FONT_NAME, 12))

addtodo = tk.Button(text="Add", font=(FONT_NAME, 8), command=new_task)
addtodo.config(bg=PINK, activebackground=PINK, width=5)

deltodo = tk.Button(text="Delete", font=(FONT_NAME, 8), command=del_task)
deltodo.config(bg=PINK, activebackground=PINK, width=5)

# GUi grid
start_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)
check_mark.grid(row=3, column=1)
todo_label.grid(row=4,column=1)
list_box.grid(row=5, column=1)
todo_entry.grid(row=6, column=1)
addtodo.grid(row=7, column=2)
deltodo.grid(row=8, column=2)

window.mainloop()