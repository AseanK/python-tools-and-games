import random

wordList = ["glide", "coffee", "chocolate"]

word = random.choice(wordList)
tries = 6
blank = []

for i in word:
    blank += "_"

print(blank)

gameOver = False
while not gameOver:
    inp = input("Choose: ")
    for i in range(len(word)):
        if inp == word[i]:
            blank[i] = word[i]

    print(blank)
    if inp not in word:
        tries -= 1
        print(f"remaining tries = {tries}")
    if "_" not in blank:
        gameOver = True
        print("you win")
    if tries < 1:
        gameOver = True
        print('you lose')


