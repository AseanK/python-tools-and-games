import unittest
from logic import Logic
from player import Player
from dice import Dice


class TestLogic(unittest.TestCase):
    def setUp(self):
        self.logic = Logic(Player(100), Dice())

    def test_role_condition(self):
        """Test that the role_condition function correctly returns the score and message"""

        # Test for Pinzoro (1, 1, 1)
        result, message = self.logic.role_condition([1, 1, 1])
        self.assertEqual(result, 5)
        self.assertEqual(message, '1 - 1 - 1  Wow Pinzoro! Congratulations!!')

        # Test for Triplet (3, 3, 3)
        result, message = self.logic.role_condition([3, 3, 3])
        self.assertEqual(result, 3)

        # Test for Jigoro (4, 5, 6)
        result, message = self.logic.role_condition([4, 5, 6])
        self.assertEqual(result, 2)
        self.assertEqual(message, '4 - 5 - 6  It is JIGORO!')

        # Test for Normal (2, 2, 3)
        result, message = self.logic.role_condition([2, 2, 3])
        self.assertEqual(result, 1)
        self.assertEqual(message, '2 - 2 - 3')

        # Test for No Role (2, 5, 6)
        result, message = self.logic.role_condition([2, 5, 6])
        self.assertEqual(result, -1)
        self.assertEqual(message, '2 - 5 - 6')

        # Test for Hifumi (1, 2, 3)
        result, message = self.logic.role_condition([1, 2, 3])
        self.assertEqual(result, -2)
        self.assertEqual(message, '1 - 2 - 3  Oh... It is HIFUMI')

    def test_draw_condition(self):
        """Test that the draw_condition function correctly identifies a draw
        and that the calculate_payment function correctly returns 0 for a draw"""

        # Test for True
        player_roll = [2, 4, 6]
        dealer_roll = [2, 4, 6]
        bet = 50
        self.assertEqual(self.logic.draw_condition(player_roll, dealer_roll), True)
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, 0)

        # Test for False
        player_roll = [2, 4, 6]
        dealer_roll = [1, 4, 6]
        self.assertEqual(self.logic.draw_condition(player_roll, dealer_roll), False)

    def test_compare_normal_condition(self):
        """Test that the compare_same_role function handles Normal correctly
        and the calculate_payment function correctly returns dividend"""
        player_roll = [2, 6, 6]
        dealer_roll = [3, 3, 5]
        bet = 50
        result = self.logic.compare_same_role(player_roll, dealer_roll)
        self.assertEqual(result, -1)
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, -50)

        player_roll = [4, 4, 6]
        dealer_roll = [2, 2, 6]
        result = self.logic.compare_same_role(player_roll, dealer_roll)
        self.assertEqual(result, 1)
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, 50)

    def test_compare_triplet_condition(self):
        """Test that the compare_same_role function handles Triplet correctly
        and the calculate_payment function returns correct dividend"""
        player_roll = [6, 6, 6]
        dealer_roll = [2, 2, 2]
        bet = 50
        result = self.logic.compare_same_role(player_roll, dealer_roll)
        self.assertEqual(result, 3)
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, 150)

    def test_calculate_win_payment(self):
        """Test that the calculate_payment function correctly calculates the win dividend"""
        player_roll = [2, 2, 2]
        dealer_roll = [4, 5, 6]
        bet = 50
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, 150)

    def test_calculate_lose_payment(self):
        """Test that the calculate_payment function correctly calculates the loss dividend."""
        player_roll = [4, 5, 6]
        dealer_roll = [2, 2, 2]
        bet = 50
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, -50)

    def test_calculate_lose_payment_negative(self):
        """Test that the calculate_payment function correctly calculates the dividend based on the negative score"""
        player_roll = [1, 2, 3]
        dealer_roll = [2, 3, 4]
        bet = 50
        dividend = self.logic.calculate_payment(player_roll, dealer_roll, bet)
        self.assertEqual(dividend, -100)


if __name__ == '__main__':
    unittest.main()
