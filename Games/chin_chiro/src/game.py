from player import Player
from dice import Dice
from logic import Logic


class GameLoop:
    def __init__(self, initial_balance=None):
        self.player = Player(initial_balance)
        self.dice = Dice()
        self.logic = Logic(self.player, self.dice)

    def run_game(self):
        while self.player.balance > 0:
            bet = self.player.set_bet()

            input('Press enter to roll the dice...')

            player_roll = self.dice.roll_dice()
            dealer_roll = self.dice.roll_dice()

            player_result, player_message = self.logic.roles_condition(player_roll)

            print(f'\nYour rolled: {player_message}')
            print(f'Dealer rolled: {dealer_roll[0]} - {dealer_roll[1]} - {dealer_roll[2]}\n')

            result = self.logic.calculate_payment(player_roll, dealer_roll, bet)
            self.player.get_current_balance(result)
            print(f'Your current balance: ${self.player.balance}\n')

            if self.player.balance <= 0:
                print("You're out of money! Game over.")
                break

            if not self.player.ask_continue():
                print("Thanks for playing!")
                break
