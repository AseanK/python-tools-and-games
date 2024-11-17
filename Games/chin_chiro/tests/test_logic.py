import unittest
from logic import Logic
from player import Player
from dice import Dice


class TestLogic(unittest.TestCase):
    def setUp(self):
        self.logic = Logic(Player(100), Dice())

    def test_roles_condition(self):
        result, message = self.logic.roles_condition([1, 1, 1])
        self.assertEqual(result, 5)
        self.assertEqual(message, '1 - 1 - 1  One pair, congrats!!')
        result, message = self.logic.roles_condition([3, 3, 3])
        self.assertEqual(result, 3)
        result, message = self.logic.roles_condition((4, 5, 6))
        self.assertEqual(result, 2)
        self.assertEqual(message, '4 - 5 - 6  It is JIGORO!')
        result, message = self.logic.roles_condition((2, 2, 3))
        self.assertEqual(result, 1)
        self.assertEqual(message, '2 - 2 - 3')
        result, message = self.logic.roles_condition([2, 5, 6])
        self.assertEqual(result, -1)
        self.assertEqual(message, '2 - 5 - 6')
        result, message = self.logic.roles_condition([1, 2, 3])
        self.assertEqual(result, -2)
        self.assertEqual(message, '1 - 2 - 3  Oh... It is HIFUMI')

    def test_draw_condition(self):
        player_roll = [2, 4, 6]
        dealer_roll = [2, 4, 6]
        bet = 50
        self.assertEqual(self.logic.draw_condition(player_roll, dealer_roll), True)
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, 0)

        player_roll = [2, 4, 6]
        dealer_roll = [1, 4, 6]
        self.assertEqual(self.logic.draw_condition(player_roll, dealer_roll), False)

    def test_compare_normal_condition(self):
        player_roll = [2, 6, 6]
        dealer_roll = [3, 3, 5]
        bet = 50
        result = self.logic.compare_same_roles(player_roll, dealer_roll)
        self.assertEqual(result, -1)
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, -50)

        player_roll = [4, 4, 6]
        dealer_roll = [2, 2, 6]
        result = self.logic.compare_same_roles(player_roll, dealer_roll)
        self.assertEqual(result, 1)
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, 50)

    def test_compare_pair_condition(self):
        player_roll = [6, 6, 6]
        dealer_roll = [2, 2, 2]
        bet = 50
        result = self.logic.compare_same_roles(player_roll, dealer_roll)
        self.assertEqual(result, 3)
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, 150)

    def test_calculate_win_payment(self):
        player_roll = [2, 2, 2]
        dealer_roll = [4, 5, 6]
        bet = 50
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, 150)

    def test_calculate_lose_payment(self):
        player_roll = [4, 5, 6]
        dealer_roll = [2, 2, 2]
        bet = 50
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, -50)

    def test_calculate_lose_payment_negative(self):
        player_roll = [1, 2, 3]
        dealer_roll = [2, 3, 4]
        bet = 50
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, -100)


if __name__ == '__main__':
    unittest.main()
