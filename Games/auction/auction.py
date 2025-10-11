import os
from sys import platform
from ascii_art import logo
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
players = {}

# Calculates average of total and selects winner
def calcBid(players):
    totalBid = []
    totalValue = 0

    for i in players:
        totalBid.append(players[i])
        totalValue += players[i]

    mean = totalValue / len(players)
    winnerBid = min(totalBid, key=lambda x:abs(x-mean))

    nameList = list(players.keys())
    bidList = list(players.values())

    position = bidList.index(winnerBid)

    winnerName = nameList[position]

    for i in players:
        print(f"{i} bid ${players[i]}")
    
    print(f"\nThe average of total comes to {mean}")
    print(f"Winner is {winnerName} with ${winnerBid}!!\n\n")

clear()

print(logo)

#Add player
bidding = True
while bidding:
    name = input("Enter your name\n")

    
    if name in players:
        print("This name is already taken")
        continue 

    while True:
        bidAmount = input("Enter the bidding amount\n$")
        if bidAmount.isdigit():
            bidAmount = int(bidAmount)
            if bidAmount > 0:
                break
            else:
                print("You have to bid more than $0")
        else:
            print(f"{bidAmount} is not a number")

    players[name] = bidAmount

    cont = (input("Add another player?\nEnter 'Yes' or 'No'\n")).lower()

    clear()

    if cont == "yes":
        continue
    if cont == "no":
        bidding = False

calcBid(players)
