import unittest
from unittest.mock import patch
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(initial_balance=100)

    @patch('builtins.input', side_effect=['-10', 'a', '100'])
    def test_set_initial_balance(self, mock_input):
        self.player.set_initial_balance()
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(self.player.balance, 100)

    @patch('builtins.input', side_effect=['-10', 'a', '200', '50'])
    def test_set_bet(self, mock_input):
        self.player.balance = 100
        bet = self.player.set_bet()
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(bet, 50)

    def test_get_current_balance(self):
        self.player.balance = 100
        self.player.get_current_balance(50)
        self.assertEqual(self.player.balance, 150)
        self.player.get_current_balance(-50)
        self.assertEqual(self.player.balance, 100)

    @patch('builtins.input', side_effect=['a', 'y'])
    def test_ask_continue(self, mock_input):
        choice = self.player.ask_continue()
        self.assertEqual(mock_input.call_count, 2)
        self.assertTrue(choice)


if __name__ == '__main__':
    unittest.main()
