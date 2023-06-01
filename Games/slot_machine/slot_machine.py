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

# Amount of symbols in the pool
number_of_symbols = {
    "⭐": 8,
    "🟢": 10,
    "🟨": 13,
    "🔷": 14,
    "🔺": 15
}

# Values of the symbols
value_of_symbols = {
    "⭐": 10,
    "🟢": 7,
    "🟨": 5,
    "🔷": 3,
    "🔺": 2
}


# Gets player's deposit
def deposit():
    while True:
        balance = input("Please enter the amount you want to deposit: $")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("\nYou must deposit more than $0")
        else:
            print(f"\n{balance} is not a number!")
    return balance


# Get player's betting
def get_bet():
    while True:
        bet = input("\nPlease enter desire betting amount: $")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print("\nYou must bet more than $0")
        else:
            print(f"\n{bet} is not a number!")
    return bet


# Chooses 3 random symbols from the pool
def get_spin(symbols):
    all_symbols = []

    for symbol, number_of_symbols in symbols.items():
        for _ in range(number_of_symbols):
            all_symbols.append(symbol)
    
    row = []
    current_symbol = all_symbols[:]
    for _ in range(1, 4):
        value = random.choice(current_symbol)
        current_symbol.remove(value)
        row.append(value)
    return row


# spinning effect display
def spin_display(symbols):
    all_symbols = []
    for symbol, number_of_symbols in symbols.items():
        for _ in range(number_of_symbols):
            all_symbols.append(symbol)
    display = []
    for _ in range(0,30):
        sleep(0.1)
        display1 = random.choice(all_symbols)
        print(display1, end=" | ")
        display2 = random.choice(all_symbols)
        print(display2, end=" | ")
        display3 = random.choice(all_symbols)
        print(display3, end="\r")


# main function
def main():
    depo = deposit()

    while True:
        print(f"\nYour current balance is {depo}\n\n")
        ans = input("Press enter to spin ('q' to quit)")
        if ans == "q":
            exit()

        while True:
            bet = get_bet()
            if bet <= depo:
                break
            else:
                print(f"\nYour current balance is {depo}\nYou cannot bet more than your balance!")
        clear()
        depo -= bet

        print("\nGOOD LUCK!")

        spin_display(number_of_symbols)

        row = get_spin(number_of_symbols)

        print(f"{row[0]} | {row[1]} | {row[2]}\n", end="\r")

        if row[0] == row[1] and row[1] == row[2]:
            value = value_of_symbols.get(row[0])
            depo += value * bet
 
        if depo <= 0:
            print("\nYou've lost all of your money!")
            ans = input("\nPress enter to deposit more or 'q' to quit")
            if ans == "q":
                print("\nThank you for playing!")
                exit()
            else:
                main()

clear()
print("Welcome to THE Slot machine!")
print('''
Winning prizes
   ⭐ : X10
   🟢 : X7
   🟨 : X5
   🔷 : X3
   🔺 : X2
''')
main()