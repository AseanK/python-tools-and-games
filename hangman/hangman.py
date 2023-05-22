import random
from asciiart import *
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

word = random.choice(word_list)
tries = 6
blank = []
word_length = len(word)

clear()
print(logo)

for i in word:
    blank += "_"

print(blank)
gameOver = False
while not gameOver:
    guess = input("Guess a letter: ").lower()

    if guess in blank:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            blank[position] = letter

    #Check if user is wrong.
    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        tries -= 1
        if tries == 0:
            gameOver = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(blank)}")

    #Check if user has got all letters.
    if "_" not in blank:
        gameOver = True
        print("You win.")

    print(stages[tries])
