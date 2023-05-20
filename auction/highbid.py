import os
from sys import platform

    # Clear command line
if platform == "linux" or platform == "linux2" or platform == "darwin":
    # linux
    os.system("clear")
if platform == "win32":
    # Windows...
    os.system("CLS")

# Global val
players = []
winner = [{"name": "none", "money": 0}]

# Calculates the highest bid
def calcBid(player):
    for i in player:
        if i["money"] > winner[0]["money"]:
            winner[0] = i

# Adds player
def add(name, money):
    players.append({"name": name, "money": money})

bidding = True

while bidding:
    name = input("Enter your name: \n")
    money = float(input("Enter the bid amount:\n$"))
    add(name,money)

    conti = input("Another player?\n'Yes' or 'No': ").lower()

        # Clear command line
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # linux
        os.system("clear")
    if platform == "win32":
        # Windows...
        os.system("CLS")

    if conti == "no":
        bidding = False
    elif conti == "yes":
        continue
    else:
        print("Invalid input \n Please try again")
        continue

calcBid(players)

winnerName = winner[0]["name"]
winnerMoney = winner[0]["money"]

for i in range(len(players)):
    print(f'{players[i]["name"]} bidded ${players[i]["money"]}')

print(f"\nwinner is {winnerName} with ${winnerMoney}")