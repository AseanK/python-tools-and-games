import turtle
import random
from time import sleep
import os
from sys import platform

# Clears command line
def clear():
    if platform == "linux" or platform == "linux2":
        # linux
        os.system("clear")
    elif platform == "darwin":
        # OS X
        os.system("clear")
    elif platform == "win32":
        # Windows...
        os.system("CLS")


TURTLES = ["red", "orange", "yellow", "green", "blue", "purple", "black"]


# Intro
def intro():
    clear()
    print("Welcome to Turtle raing bet!")
    print("""\nRules are simple
    Enter a color of the turtle
    Place the amount you want to bet
    Watch your turtle win! or lose
    """)
    inp = input("Press enter to start, 'q' to quit")
    if inp == 'q':
        exit()


# Get user's betting choice
def get_turtle():
    while True:
        inp = input("""
Choose a trutle you want to bet:

Red    Orange    Yellow    Green    Blue    Purple    Black\n""").lower()
        if inp in TURTLES:
            break
        else:
            print("Please enter from the choice")
    return inp


# Get user's bet
def get_bet():
    while True:
        inp = input("Enter a amount you want to bet\n$")
        if inp.isdigit():
            inp = int(inp)
            if inp > 0:
                break
            else:
                print("You have to bet more than $0")
        else:
            print(f"{inp} is not a number!")
    return inp


# Count down before the game starts 
def count_down():
    for i in range(5,0, -1):
        print(f"Race starts in ...{i}", end="\r")
        sleep(.7)


# Turtle racing main, returns the winner color
def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("gray")

    all_turtles = []
    position = -270

    for each_turtle in TURTLES:
        new_turtle = turtle.Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(each_turtle)
        new_turtle.pu()
        new_turtle.goto(-270, position)
        position += 90
        all_turtles.append(new_turtle)

    while True:
        for t in all_turtles:
            if t.xcor() > 260:
                winner = t.pencolor()
                screen.bye()
                return winner

            speed = random.randint(0, 10)
            t.fd(speed)


# Count down before the winner reveal
def print_winner():
    dots = ".", "..", "..."
    for dot in dots:
        print(f"The winner is {dot}", end="\r")
        sleep(1)


# Play game, display if the user guessed it right
def start():
    user_guess = get_turtle()
    user_bet = get_bet()
    count_down()
    clear()
    print("GOOD LUCK!")
    winner = main()
    clear()
    print_winner()

    print(f"The winner is {winner.upper()}!!!")
    if winner == user_guess:
        print(f"\nCONGRATS!! You Won ${user_bet * 3}!")
    else:
        print(f"\nYou lost ${user_bet} 😓")
        print("\nBetter luck next time!")
        exit()

intro()
clear()
start()
