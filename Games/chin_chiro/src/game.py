from player import Player
from dice import Dice
from logic import Logic


class GameLoop:
    """
    GameLoop class manages the main game loop.
    The loop continues as long as the player has positive balance.
    """
    def __init__(self, initial_balance=None):
        self.player = Player(initial_balance)
        self.dice = Dice()
        self.logic = Logic(self.player, self.dice)

    def run_game(self):
        """
        Runs the game loop.
        The loop continues as long as the player has money and chooses to continue playing.
        """
        # Continue the game if the player's balance is positive.
        while self.player.balance > 0:
            bet = self.player.set_bet()

            input('Press enter to roll the dice...')

            player_roll = self.dice.roll_dice()
            dealer_roll = self.dice.roll_dice()

            # Evaluate the player's roll and generate the result.
            player_result, player_message = self.logic.role_condition(player_roll)

            print(f'\nYour rolled: {player_message}')
            print(f'Dealer rolled: {dealer_roll[0]} - {dealer_roll[1]} - {dealer_roll[2]}\n')

            # Calculate the dividend based on the score and update the player's balance.
            result = self.logic.calculate_payment(player_roll, dealer_roll, bet)
            self.player.get_current_balance(result)
            print(f'Your current balance: ${self.player.balance}\n')

            # If the player has no money left, end the game.
            if self.player.balance <= 0:
                print("You're out of money! Game over.")
                break

            # Exit the game loop if the player chooses 'n' in ask_continue prompt
            if not self.player.ask_continue():
                print("Thanks for playing!")
                break
