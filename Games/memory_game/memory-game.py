import random
import os
import time

class MemoryGame:
    def __init__(self, size=4):
        self.size = size
        self.symbols = ['🌟', '🌙', '🌍', '🌈', '🌺', '🍀', '🎵', '🎨'][:size*size//2] * 2
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.shuffle_board()
    
    def play(self):
        pairs_found = 0
        moves = 0
        
        while pairs_found < (self.size * self.size) // 2:
            self.display_board()
            print(f"\nMoves: {moves} | Pairs found: {pairs_found}")
            
            # First card
            row1, col1 = self.get_move()
            self.revealed[row1][col1] = True
            self.display_board()
            
            # Second card
            row2, col2 = self.get_move()
            self.revealed[row2][col2] = True
            self.display_board()
            
            moves += 1
            
            # Check if pair matches
            if self.board[row1][col1] == self.board[row2][col2]:
                pairs_found += 1
                print("Match found!")
            else:
                print("No match...")
                self.revealed[row1][col1] = False
                self.revealed[row2][col2] = False
            
            time.sleep(1)
        
        print(f"\nCongratulations! You won in {moves} moves!")

if __name__ == "__main__":
    game = MemoryGame()
    game.play()