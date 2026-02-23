import os
from sys import platform

from utils import package_installer
package_installer.install_dependencies()

import pandas


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

    print("Welcome to NATO phonetic alphabet translator!\n")
    print("A spelling alphabet is a set of words used to stand for the letters of an alphabet in oral communication")
    print("It is used to spell out words when speaking to someone not able to see the speaker,\nor when the audio channel is not clear")
    print("Enter a word and this program will translate it for you!\n")


nato = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}

clear()

# Input validation
while True:
    inp = input("Enter a word: ").upper()
    if not inp.isalpha():
        print("Only letters are allowed, no symbols, or empty space or numbers...")
    elif inp == "QUIT":
        break

    ans = [nato_dict[letter] for letter in inp if letter != " "]
    print([nato_dict[letter] for letter in inp if letter != " "])

# Added single check statement that will check if letter is entered
# Removed redundant while loop (outer) because there is no way to break out of program once you start it
# Removed redundant quit statement in Intro() function
# Moved intro() inside single function as its all prints statements