import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deposit():
    while True:
        balance = input("How much would you like to deposit?  $")
        if balance.isdigit:
            balance = int(balance)
            if balance < 0:
                return balance
            if balance > 0:
                break
            else:
                print("You can't deposit $0")
        else:
            print(f"{balance} is not a number")


def get_bet():
    while True:
        amount = input("How much would you like to bet?  $")
        if amount.isdigit:
            amount = int(amount)
            if amount < 0:
                return amount
            if amount > 0:
                break
            else:
                print("You can't bet $0")
        else:
            print(f"{amount} is not a number")


def deal_card():
    card = random.choice(CARDS)
    return card


def calcScore(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def checkWinner(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "    You lose, you went over. 😤"
    
    if user_score == computer_score:
        return "    Draw 🙃"
    elif computer_score == 0:
        return "    You lose, dealer has Blackjack 😱"
    elif user_score == 0:
        return "    You Win with a Blackjack 😎"
    elif user_score > 21:
        return "    You lose, you went over 😭"
    elif computer_score > 21:
        return "    You win, dealer went over 😁"
    elif user_score > computer_score:
        return "    You win 😃"
    else:
        return "    You lose 😤"

def play_game():
    while True:
        play = input("Press enter to play ('q' to quit)")
        if play =="q":
            exit()
        balance = deposit()
        print(f"Your current balance is ${balance}")
      
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
            print(f"   Computer's first card: {computer_cards[0]}")
      
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
        print(checkWinner(user_score, computer_score))
    


play_game()