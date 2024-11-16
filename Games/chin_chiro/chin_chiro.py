import random
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


def dice():
  a = random.randint(1, 6)
  b = random.randint(1, 6)
  c = random.randint(1, 6)
  return a, b, c


def roles_condition(a, b, c):
    if a == b == c == 1:
        print(f'{a}-{b}-{c}: One pair, congrats!!')
        return 5
    elif a == b == c != 1:
        print(f'{a}-{b}-{c}')
        return 3
    elif a != b != c and a + b + c == 15:
        print(f'{a}-{b}-{c}: JIGORO')
        return 2
    elif a == b != c:
        print(f'{a}-{b}-{c}')
        return 1
    elif b == c != a:
        print(f'{a}-{b}-{c}')
        return 1
    elif c == a != b:
        print(f'{a}-{b}-{c}')
        return 1
    elif a != b != c and a + b + c == 6:
        print(f'{a}-{b}-{c}: HIFUMI')
        return -2
    else:
        print(f'{a}-{b}-{c}')
        return -1

# set initial balance
def set_balance():
    while True:
        initial_balance = input('Your initial balance: $')
        if initial_balance.isdigit():
            initial_balance = int(initial_balance)
            if initial_balance > 0:
                return initial_balance
            else:
                print('Set balance must be greater than 0.')
        else:
            print('Enter numbers greater than 0.')

# Set player's bet amount
def set_bet(balance):
    while True:
        bet_amount = input('Your bet amount: $')
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if 0 < bet_amount <= balance:
                return bet_amount
            else:
                print(f'Set your bet between 0 and your balance: ${balance}')
        else:
            print('Enter numbers greater than 0.')

# Player dices
def roll_for_player():
    print("Your turn")
    player_roll = dice()
    return player_roll

# Dealer dices
def roll_for_dealer():
    print("Dealer's turn")
    dealer_roll = dice()
    return dealer_roll

# Select continue or quit
def ask_continue():
    while True:
        continue_choice = input("Do you want to continue (y/n)? ").lower()
        if continue_choice == 'y':
            return True
        elif continue_choice == 'n':
            return False
        else:
            print("Please enter y or n")


# Draw condition
def draw_condition(player_roll, dealer_roll):
    if player_roll == dealer_roll:
        return True
    return False


# Compare normal roles if player and dealer have pairs
def compare_normal_condition(player_roll, dealer_roll):
    player_result = sorted(player_roll)
    dealer_result = sorted(dealer_roll)

    # Check pairs, count twice existing number
    player_pairs = [num for num in player_roll if player_roll.count(num) == 2]
    dealer_pairs = [num for num in dealer_roll if dealer_roll.count(num) == 2]

    if player_pairs and dealer_pairs:
        # Compare no pair numbers
        player_other = [num for num in player_roll if player_roll.count(num) == 1][0]
        dealer_other = [num for num in dealer_roll if dealer_roll.count(num) == 1][0]

        # Win if the other number is smaller
        if player_other < dealer_other:
            print("You won! You got 1x your bet.")
            return 1
        elif player_other > dealer_other:
            print("You lose. You lost -1x your bet.")
            return -1
        else:
            # Smaller total is win if other number is same
            player_sum = sum(player_roll)
            dealer_sum = sum(dealer_roll)
            if player_sum < dealer_sum:
                print("You won! You got 1x your bet.")
                return 1
            else:
                print("You lose. You lost -1x your bet.")
                return -1
    else:
        return None


def calculate_payment(player_roll, dealer_roll, balance, bet):
    player_score = roles_condition(player_roll[0], player_roll[1], player_roll[2])
    dealer_score = roles_condition(dealer_roll[0], dealer_roll[1], dealer_roll[2])

    balance -= bet
    if draw_condition(player_roll, dealer_roll):
        print("Draw, your bet is returned.")
        balance = balance + bet
        return balance

    if player_score == dealer_score == 1:
        player_score = compare_normal_condition(player_roll, dealer_roll)
        balance = balance + bet * player_score
        return balance

    # Player win condition
    if player_score > dealer_score:
        print(f'You got ${player_score}x your bet!')
        balance = balance + bet * player_score
        return balance

    # Player lose condition
    elif player_score < 0:
        print(f"You lose... ${player_score}x your bet lost")
        balance = balance + bet * player_score
        return balance

def game_loop():
    balance = set_balance()
    while True:
        bet = set_bet(balance)
        player_roll = roll_for_player()
        dealer_roll = roll_for_dealer()

        if draw_condition(player_roll, dealer_roll):
            continue

        balance = calculate_payment(player_roll, dealer_roll, balance, bet)
        print(f"Your current balance: ${balance}")

        if balance <= 0:
            print("You're out of money! Game over.")
            break

        if not ask_continue():
            print("Thanks for playing!")
            break
