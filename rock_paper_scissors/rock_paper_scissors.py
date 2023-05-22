
### ROCK PAPER SCISSORS GAME ###

# Imports
import random
from time import sleep

# Declaring variables

rockConditions: dict[str:int] = {'rock' : 0, 'paper' : -1, 'scissors' : 1}
paperConditions: dict[str:int] = {'rock' : 1, 'paper' : 0, 'scissors' : -1}
scissorConditions: dict[str:int] = {'rock' : -1, 'paper' : 1, 'scissors' : 0}

playerPath: dict[str:dict] = {'rock': rockConditions, 'paper': paperConditions, 'scissors': scissorConditions}

choices: list[str] = ['rock', 'paper', 'scissors']

player_score: int = 0
CPU_Score: int = 0
round_counter: int = 0

# Game starting

print('Welcome to Rock Paper Scissors!')

# Game loop
while True:

    CPU_Choice: str = random.choice(choices)

    player_Choice: str = input('Rock, Paper, or Scissors?\n').lower()

    # Loop will restart if player has an invalid choice
    if player_Choice not in choices:
        print("You didn't pick any options!\n")
        continue
    
    # Suspence
    print('\n')
    for item in choices:
        sleep(0.5)
        print(f'{item.title()}...')
    print('Shoot!')

    # Display Player's choice and then CPU's
    print(f'\nPlayer: {player_Choice}\nCPU: {CPU_Choice}\n')

    # Whichever the player's choice is, their value will always be 1
    # The CPU's choice will access the same dictionary as the player's to compare choices

    if playerPath[player_Choice][player_Choice] < playerPath[player_Choice][CPU_Choice]:

        print('You win!\n')
        player_score += 1

    elif playerPath[player_Choice][player_Choice] > playerPath[player_Choice][CPU_Choice]:

        print('You lose!\n')
        CPU_Score += 1

    else:
        print("It's a tie!\n")
    
    round_counter += 1

    # Displaying the player score, CPU score, and how many rounds have been played
    print(f'Player Score: {player_score}\nCPU Score: {CPU_Score}\nRounds: {round_counter}\n')
    
    # Asking the player if they want to play again
    again: str = input('Play again? (y/n)\n').lower()

    # If user input is not y the script will end
    if again != 'y':
        print('\nThanks for playing!')
        break
        

