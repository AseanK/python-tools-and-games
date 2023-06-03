import random
import os
from sys import platform
import time
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

def main():
    print("Hello!")
    time.sleep(0.5)
    print("Welcome to The Gambler Game!")
    time.sleep(1)
    balance = 100
    willing_to_quit = False
    print(f"--Your starting balance is {balance}$")
    while balance > 0 and willing_to_quit == False:
        bet = input(f"1.Make a bet, you have {balance}$, or if you want to quit press q \n")
        if bet == "q":
            willing_to_quit = True
            continue
        else:
            try:
                bet = int(bet)
            except:
                print("WRONG NUMBER,\n try again using amount affordable for your balance")
                continue
        if bet <= balance:
            guess =-1
            while guess > 3 or guess < 1:
                guess = int(input("2.Pick a cup from 1-3,\n"))
            anwser = random.randint(1,3)
            print("3.Checkcking your luck!")
            if anwser == guess:
                print("YES!YES!YES!")
                balance+=bet
            else:
                print('Wrong cup!')
                balance-=bet
            time.sleep(0.4)
        else:
            print("WRONG NUMBER,\n try again using amount affordable for your balance")
    if balance <= 0:
        print("GAME OVER!")
    elif balance > 100:
        print("GOOD JOB")
    elif balance < 100:
        print("Next time will be better")
    else:
        print("Interesting play")
if __name__ == "__main__":
    clear()
    main()