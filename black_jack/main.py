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

# Global Val
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
balance = 0
bet = 0

# Gets player's deposit
def deposit():
    while True:
        balance = input("How much would you like to deposit?  $")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("You can't deposit $0")
        else:
            print(f"{balance} is not a number")
    return balance

# Gets player's bet amount
def get_bet():
    while True:
        amount = input("How much would you like to bet?  $")
        if amount.isdigit():
            amount = int(amount)
            if amount > balance:
                print(f"You cannot bet more than your current balance (${balance})")
            elif amount > 0:
                break
            else:
                print("You can't bet $0")
        else:
            print(f"{amount} is not a number")
    return amount

# Draws card from the deck
def deal_card():
    card = random.choice(CARDS)
    return card

# Calculates total hand
def calcScore(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Checks for winner
def checkWinner(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("    You lose, you went over. 😤")
        return balance - bet
    
    if user_score == computer_score:
        print("    Draw 🙃")
        return balance
    elif computer_score == 0:
        print("    You lose, dealer has Blackjack 😱")
        return balance - bet
    elif user_score == 0:
        print("    You Win with a Blackjack 😎")
        return balance + bet
    elif user_score > 21:
        print("    You lose, you went over 😭")
        return balance - bet
    elif computer_score > 21:
        print("    You win, dealer went over 😁")
        return balance + bet
    elif user_score > computer_score:
        print("    You win 😃")
        return balance + bet
    else:
        print("    You lose 😤")
        return balance - bet

def play_game():
    global balance
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    
    while not is_game_over:
        user_score = calcScore(user_cards)
        computer_score = calcScore(computer_cards)
        print(f"\n   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Dealer's card: [{computer_cards[0]}, _ ]")
    
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("\nType 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
              user_cards.append(deal_card())
            else:
              is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calcScore(computer_cards)
    
    print(f"\n    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    balance = checkWinner(user_score, computer_score)
    


clear()
balance = deposit()
while True:
    if balance <= 0:
        print("\nYou've lost all of your money! 😭")
        exit()
    play = input("Press enter to play ('q' to quit)")
    clear()
    if play =="q":
        exit()
    balance = balance
    print(f"Your current balance is ${balance}\n")
    bet = get_bet()
    play_game()