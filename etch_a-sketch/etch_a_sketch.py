import turtle

pointer = turtle.Turtle()
screen = turtle.Screen()
colors = ["red", "blue", "green", "yellow", "orange", "black", "purple"]

def intro():
    while True:
        inp = turtle.textinput("        Etch A Sketch", 
                            """         Welcome!\n
W, A ,S D   : Move
Space         : Toggle pen
C                : Clear
E                 : Color selection

Enter 'Start' to start!
""").lower()
        if inp == 'start':
            break

def move_forward():
    pointer.fd(10)

def move_backward():
    pointer.bk(10)

def tilt_left():
    pointer.lt(10)

def tilt_right():
    pointer.rt(10)

def on_off():
    if pointer.isdown():
        pointer.penup()
    else:
        pointer.pendown()

def clear():
    turtle.resetscreen()

def color():
    while True:
        color = turtle.textinput("                    Color Selection", 
                                 "Red, Blue, Green, Yellow, Orange, Black, Purple").lower()
        if color in colors:
            break
    pointer.color(color)
    turtle.listen()

intro()
turtle.onkeypress(move_forward, "w")
turtle.onkeypress(move_backward, "s")
turtle.onkeypress(tilt_left, "a")
turtle.onkeypress(tilt_right, "d")
turtle.onkey(on_off, "space")
turtle.onkey(clear, "c")
turtle.onkey(color, "e")

turtle.listen()
turtle.mainloop()
