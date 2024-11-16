import random


class Dice:
    @staticmethod
    def roll_dice():
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        dice = [a, b, c]
        dice = sorted(dice)
        return dice

    def get_player_dice(self):
        player_roll = Dice.roll_dice()
        return player_roll

    def get_dealer_dice(self):
        dealer_roll = Dice.roll_dice()
        return dealer_roll
