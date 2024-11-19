from player import Player
from dice import Dice


class Logic:
    """
    Logic class manages the logic of the game.
    - Evaluates the role based on the dice combination.
    - Checks the win condition for the same role.
    - Calculates the dividend based on the score.
    """
    def __init__(self, player, dice):
        self.player = player
        self.dice = dice

    def role_condition(self, dice_roll):
        """
        Determines the role of the rolled dice combination.

        Args:
            dice_roll (list): A list of the dice roll.

        Return:
            int: The score of the role.
            str: The result and message describing the role.
        """
        a, b, c = dice_roll
        if a == b == c:
            if a == 1:
                result = f'{a} - {b} - {c}  Wow Pinzoro! Congratulations!!'
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
        """
        Checks the draw condition.

        Args:
            player_roll (list): A list of the player rolls
            dealer_roll (list): A list of the dealer rolls

        Returns:
            bool: True if both the player and dealer have the same dice roll, otherwise False.
        """
        if player_roll == dealer_roll:
            return True
        return False

    def compare_same_role(self, player_roll, dealer_roll):
        """
        Compares the same role to decide the winner.

        Args:
            player_roll (list): A list of the player rolls
            dealer_roll (list): A list of the dealer rolls

        Returns:
            int: The score based on the role.
        """
        # If both player and dealer have triplets, the higher wins.
        if (player_roll[0] == player_roll[1] == player_roll[2] and
                dealer_roll[0] == dealer_roll[1] == dealer_roll[2]):
            if player_roll[0] > dealer_roll[0]:
                print("You won! You got 3x your bet.")
                return 3
            elif player_roll[0] < dealer_roll[0]:
                print("You lose. You lost -1x your bet.")
                return -1
            else:
                return 0

        # Check if both have pairs to compare the score.
        player_pairs = [num for num in player_roll if player_roll.count(num) == 2]
        dealer_pairs = [num for num in dealer_roll if dealer_roll.count(num) == 2]

        if player_pairs and dealer_pairs:
            # If both have pairs, compare the non-pair numbers.
            player_other = [num for num in player_roll if player_roll.count(num) == 1][0]
            dealer_other = [num for num in dealer_roll if dealer_roll.count(num) == 1][0]

            # If the non-pair number is higher, wins.
            if player_other > dealer_other:
                print("You won! You got 1x your bet.")
                return 1
            elif player_other < dealer_other:
                print("You lose. You lost -1x your bet.")
                return -1
            else:
                # If the non-pair numbers are equal, the higher total wins.
                player_sum = sum(player_roll)
                dealer_sum = sum(dealer_roll)
                if player_sum > dealer_sum:
                    print("You won! You got 1x your bet.")
                    return 1
                else:
                    print("You lose. You lost -1x your bet.")
                    return -1
        else:
            return None  # No pair, no comparison

    def calculate_payment(self, player_roll, dealer_roll, bet):
        """
        Calculates the dividend based on the score.

        Args:
            player_roll (list): A list of the player rolls
            dealer_roll (list): A list of the dealer rolls
            bet (int): The bet set by the player

        Return:
            dividend (int): The dividend (positive or negative) based on the role.
        """
        # Determine the score for both player and dealer.
        player_score, p_message = self.role_condition(player_roll)
        dealer_score, d_message = self.role_condition(dealer_roll)

        # If it is draw, return the bet back.
        if self.draw_condition(player_roll, dealer_roll):
            print("Draw, your bet is returned.")
            dividend = 0
            return dividend

        # If the same role, compare the score using compare_same_role
        elif player_score == dealer_score == 1 or player_score == dealer_score == 3:
            player_score = self.compare_same_role(player_roll, dealer_roll)
            dividend = bet * player_score
            return dividend

        # Calculate the player's bet multiplied by the score based on the roll.
        elif player_score > dealer_score:
            print(f'You got {player_score}x your bet!')
            dividend = bet * player_score
            return dividend

        elif player_score < 0:
            print(f"You lose... {player_score}x your bet lost")
            dividend = bet * player_score
            return dividend

        elif player_score < dealer_score:
            print(f"You lose... You lost ${bet}.")
            dividend = bet * -1
            return dividend
