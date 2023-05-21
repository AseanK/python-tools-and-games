import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check(cards):
    total = 0
    for card in cards:
        total += card
    return total


def draw_card():
    player_card = []
    dealer_card = []

    player_card.append(random.choice(CARDS))
    player_card.append(random.choice(CARDS))
    dealer_card.append(random.choice(CARDS))

    print(f"Your card : {player_card}")
    print(f"Dealer's card : {dealer_card}")


    while True:
        draw = input("DRAW or STAND\n").lower()
        
        if draw == "draw":
            player_card.append(random.choice(CARDS))
            total_player = check(player_card)

            print(f"Your card : {player_card}")
            if total_player > 21:
                print("BUST!")
                exit()
            continue
        elif draw == "stand":
            break
        else:
            print(f"{draw} is not a valid input!")


    dealer_card.append(random.choice(CARDS))
    print(f"Dealer's card : {dealer_card}")

    total_dealer = check(dealer_card)
    
    while total_dealer < 17:
        dealer_card.append(random.choice(CARDS))
        total_dealer = check(dealer_card)
        print(f"Dealer's card : {dealer_card}")
    if total_dealer > 21:
        print("Dealer BUST!")
    
    print(f"Your card : {player_card} total of {total_player}")
    print(f"Dealer's card : {dealer_card} total of {total_dealer}")
    if total_player > total_dealer:
        print("You win!")
    elif total_player < total_dealer:
        print("You lose!")
    else:
        print("Draw!")
    

    

start = input("Do you want to start the game?\n'Yes' or 'No: '").lower()
if start == 'yes':
    draw_card()