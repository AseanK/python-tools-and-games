import unittest
import board_filling_game as bf


class TestBoardFillingGame(unittest.TestCase):
    # Test that the game correctly identifies that
    # the game is still ongoing.
    def test_is_game_done_empty(self):
        board = [["□", "□"], ["□", "□"]]
        self.assertFalse(bf.is_game_done(board))

    # Test that the game correctly identifies that
    # the game has been completed.
    def test_is_game_done_full(self):
        board = [["■", "■"], ["■", "■"]]
        self.assertTrue(bf.is_game_done(board))