import pandas
import re

nato = pandas.read_csv("./nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}


def intro():
    print("Welcome to NATO phonetic alphabet translator!\n")
    print("A spelling alphabet is a set of words used to stand for the letters of an alphabet in oral communication")
    print("It is used to spell out words when speaking to someone not able to see the speaker,\nor when the audio channel is not clear")
    print("Enter a word and this program will translate it for you!\n")

    inp = input("Press ENTER to start, 'q' to quit")
    if inp == "q":
        exit()

intro()

while True:

    # Input validation
    while True:
        inp = input("Enter a word: ").upper()
        if inp == '':
            print("* you haven't entered anything.")
            continue
        elif re.search('[0-9]', inp):
            print("* entry can't contain numbers. please try again with only letters.")
            continue
        elif re.search('[^\w-]|_', inp):
            print("* entry can't contain symbols. please try again with only letters.")
            continue
        else:
            break

    ans = [nato_dict[letter] for letter in inp if letter != " "]
    print(ans)