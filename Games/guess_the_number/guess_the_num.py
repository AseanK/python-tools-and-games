import random
import os
from sys import platform
from time import sleep

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

MIN = 1
MAX = 100

def get_guess():
    while True:
        player_guess = input("Choose a number: ")
        if player_guess.isdigit():
            player_guess = int(player_guess)
            if MIN < player_guess < MAX:
                break
            else:
                print("The number has to be 1 to 100")
        else:
            print(f"{player_guess} is not a number!")
    return player_guess


def get_randint():
    random_number = random.randint(0,100)
    return random_number

def get_lucky():
    lucky_num = random.randint(1, 10)
    return lucky_num


def mode():
    while True:
        print("Easy: 10 chances | Hard: 5 chances")
        print("You're feeling extremely lucky? try `LUCKY`\n")
        mode = input("Choose your difficulty level\n'Easy'  'Hard'  'LUCKY' : ")
        if isinstance(mode, str):
            mode = mode.lower()
            if mode == "easy" or mode == "hard" or mode == "lucky":
                break
            else:
                print("You have to choose 'easy'  'hard'  'lucky'!")
        else:
            print("You hav to choose 'easy'  'hard'  'lucky'!")
    return mode


def main():
    lives = 0 

    while True:
        play = input("Press enter to play (`q` to quit)")
        clear()
        if play == "q":
            exit()

        level = mode()
        if level == "easy":
            lives = 10
        elif level == "hard":
            lives = 5
        else:
            lives = 1
            ans = get_lucky()
            clear()
            print("You have ONLY 1 chance to guess the number")
            print("The number is between 1 to 50")
            print("Let's see how lucky you are")
            
            guess = get_guess()
            if guess == ans:
                print("       CONGRATS!")
                print("WOW you really are lucky!")
                print("possibility was 2%")
            else:
                print(f"The number was {ans}")
            
            for i in range(5, 0, -1):
                sleep(1)
                print(f"Restarting the game in {i} seconds...", end="\r")
            clear()
            main()

        
        ans = get_randint()
        
        while lives > 0:
            guess = get_guess()
            lives -= 1
            if guess == ans:
                print("Congrats! you win the game!")
                break
            elif guess > ans:
                print(f"\nLower than {guess}\n")
                print(f"Remaining guess: {lives}")
            else:
                print(f"\nHigher than {guess}\n")
                print(f"Remaining guess: {lives}")

        if lives == 0:
            print(f"\nThe number was {ans}!")

        for i in range(5, 0, -1):
            sleep(1)
            print(f"Restarting the game in {i} seconds...", end="\r")
        clear()
        main()

        
clear()
print("                        Welcome to Geuss The Number!")
print("Rules are simple, I'll choose a number 1 to 100 and you have to guess it right!\n")
main()