import random


class Dice:
    """
    Dice class provides methods to simulate rolling three dice.
    The result are returned as a sorted list of random numbers between 1 and 6.
    """
    @staticmethod
    def roll_dice():
        """
        Rolls three dice and returns their result sorted.
        All dice rolls are random and within the range of 1 to 6.

        Returns:
            list: A sorted integer list of dice rolls.
        """
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        dice = [a, b, c]
        dice = sorted(dice)
        return dice

    def get_player_dice(self):
        """
        Rolls the dice for the player and returns the result.

        Returns:
            list: A sorted integer list of dice rolls.
        """
        player_roll = Dice.roll_dice()
        return player_roll

    def get_dealer_dice(self):
        """
        Rolls the dice for the dealer and returns the result.

        Returns:
            list: A sorted integer list of dice rolls.
        """
        dealer_roll = Dice.roll_dice()
        return dealer_roll
