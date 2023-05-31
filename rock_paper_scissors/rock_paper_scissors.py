import os
import random
from time import sleep

choices = ['rock', 'paper', 'scissors']

player_score = 0
cpu_score = 0
round_counter = 0

clear = lambda: os.system('cls')

print('Welcome to Rock Paper Scissors!')

while True:
    cpu_choice = random.choice(choices)

    player_choice = input('Rock, Paper, or Scissors?\n').lower()

    if player_choice not in choices:
        print("Invalid choice. Please pick from 'rock', 'paper', or 'scissors'.\n")
        continue

    print('\n')
    for item in choices:
        print(f'{item.title()}...')
        sleep(0.5)
    print('Shoot!')

    print(f'\nPlayer: {player_choice}\nCPU: {cpu_choice}\n')

    if player_choice == cpu_choice:
        print("It's a tie!\n")
    elif (choices.index(player_choice) - choices.index(cpu_choice)) % 3 == 1:
        print('You win!\n')
        player_score += 1
    else:
        print('You lose!\n')
        cpu_score += 1

    round_counter += 1

    print(f'Player Score: {player_score}\nCPU Score: {cpu_score}\nRounds: {round_counter}\n')

    again = input('Play again? (y/n)\n').lower()

    clear()

    if again != 'y':
        print('\nThanks for playing!')
        sleep(2.5)
        break
