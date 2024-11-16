from player import Player
from dice import Dice


class Logic:
    def __init__(self, player, dice):
        self.player = player
        self.dice = dice

    def roles_condition(self, dice_roll):
        a, b, c = dice_roll
        if a == b == c:
            if a == 1:
                result = f'{a} - {b} - {c}: One pair, congrats!!'
                return 5, result
            result = f'{a} - {b} - {c}'
            return 3, result
        elif a != b != c and a + b + c == 15:
            result = f'{a} - {b} - {c}  It is JIGORO!'
            return 2, result
        elif a == b != c:
            result = f'{a} - {b} - {c}'
            return 1, result
        elif b == c != a:
            result = f'{a} - {b} - {c}'
            return 1, result
        elif c == a != b:
            result = f'{a} - {b} - {c}'
            return 1, result
        elif a != b != c and a + b + c == 6:
            result = f'{a} - {b} - {c}  Oh... It is HIFUMI'
            return -2, result
        else:
            result = f'{a} - {b} - {c}'
            return -1, result

    def draw_condition(self, player_roll, dealer_roll):
        if player_roll == dealer_roll:
            return True
        return False

    def compare_normal_condition(self, player_roll, dealer_roll):
        player_pairs = [num for num in player_roll if player_roll.count(num) == 2]
        dealer_pairs = [num for num in dealer_roll if dealer_roll.count(num) == 2]

        if player_pairs and dealer_pairs:
            # Compare no pair numbers
            player_other = [num for num in player_roll if player_roll.count(num) == 1][0]
            dealer_other = [num for num in dealer_roll if dealer_roll.count(num) == 1][0]

            # Win if the other number is smaller
            if player_other < dealer_other:
                print("You won! You got 1x your bet.")
                return 1
            elif player_other > dealer_other:
                print("You lose. You lost -1x your bet.")
                return -1
            else:
                # Smaller total is win if other number is same
                player_sum = sum(player_roll)
                dealer_sum = sum(dealer_roll)
                if player_sum < dealer_sum:
                    print("You won! You got 1x your bet.")
                    return 1
                else:
                    print("You lose. You lost -1x your bet.")
                    return -1
        else:
            return None

    def calculate_payment(self, player_roll, dealer_roll, bet):
        player_score, p_message = self.roles_condition(player_roll)
        dealer_score, d_message = self.roles_condition(dealer_roll)

        if self.draw_condition(player_roll, dealer_roll):
            print("Draw, your bet is returned.")
            dividend = 0
            return dividend

        elif player_score == dealer_score == 1:
            player_score = self.compare_normal_condition(player_roll, dealer_roll)
            dividend = bet * player_score
            return dividend

        elif player_score > dealer_score:
            print(f'You got {player_score}x your bet!')
            dividend = bet * player_score
            return dividend

        elif player_score < dealer_score and 0 < player_score:
            print(f"You lose... ${bet} lost")
            dividend = bet * -1
            return dividend

        elif player_score < 0:
            print(f"You lose... {player_score}x your bet lost")
            dividend = bet * player_score
            return dividend
