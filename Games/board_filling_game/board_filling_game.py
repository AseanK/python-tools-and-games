import os
from sys import platform
from random import randint

# Clears command line
def clear():
    if platform == "linux" or platform == "linux2":
        # linux
        os.system("clear")
    elif platform == "darwin":
        # OS X
        os.system("clear")
    elif platform == "win32":
        # Windows
        os.system("CLS")

# Welcomes the player and sets up the board sizes
def welcome():
    print("Welcome to Board Filling Game.")
    print("Rules: ")
    print("1. Enter coordinates to put the pieces on the board.")
    print("2. Enter (0, 0) to skip the round.")
    print("3. Try to fill the board in as few rounds as possible!\n")

    print("Please enter the board size you want.")
    height = 3
    width = 3
    try:
        height = int(input("Height (default: 3) -> "))
        width = int(input("Width (default: 3) -> "))
    except:
        print("Invalid height. Using a 3x3 board as default.")
        height = 3
        width = 3
    
    return height, width

# Checks if there are any empty cells left
def is_game_done(game_board):
    for row in game_board:
        for cell in row:
            if cell == "□":
                return False
    
    return True

def print_board(game_board):
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()

# Prints the piece onto the game screen
def print_piece(current_piece):
    result = ""

    if current_piece == 0:
        result = "■"
    elif current_piece == 1:
        result = "■ ■"
    elif current_piece == 2:
        result = "■\n■"
    elif current_piece == 3:
        result = "■ ■ ■"
    elif current_piece == 4:
        result = "■\n■\n■"
    
    print(result)

# Gets player input, retrying if necessary
def get_player_input():
    
    x = -1
    y = -1

    print()
    while x < 0 or y < 0:
        try:
            x = int(input("Column -> "))
            y = int(input("Row -> "))
        except:
            print("Invalid coordinates. Please re-enter.")

    return x, y

# Updates the board
def update_board(game_board, height, width, x, y, current_piece):
    # Convert from 1-indexed to 0-indexed coordinates
    x = x - 1
    y = y - 1

    # If the coordinates are out of range     
    if x<-1 or x>=width or y<-1 or y>=height:
        print("Invalid coordinates. Skipping turn...")
        return game_board
    elif x == -1 or y == -1:
        print("Skipping turn...")
    
    # Coordinates are not out of range, check whether the piece fits into the board
    new_board = game_board

    # 0: x
    if current_piece == 0 and game_board[y][x]=="□":
        new_board[y][x] = "■"
    
    # 1: xx horizontal
    elif current_piece == 1 and x+1<width and game_board[y][x]=="□" and game_board[y][x+1]=="□":
        game_board[y][x] = "■"
        game_board[y][x+1] = "■"

    # 2: xx vertical
    elif current_piece == 2 and y+1<height and game_board[y][x]=="□" and game_board[y+1][x]=="□":
        game_board[y][x] = "■"
        game_board[y+1][x] = "■"

    # 3: xxx horizontal
    elif current_piece == 3 and x+2<width and game_board[y][x]=="□" and game_board[y][x+1]=="□" and game_board[y][x+2]=="□":
        game_board[y][x] = "■"
        game_board[y][x+1] = "■"
        game_board[y][x+2] = "■"

    # 4: xxx vertical
    elif current_piece == 4 and y+2<height and game_board[y][x]=="□" and game_board[y+1][x]=="□" and game_board[y+2][x]=="□":
        game_board[y][x] = "■"
        game_board[y+1][x] = "■"
        game_board[y+2][x] = "■"


    return new_board

if __name__=="__main__":

    # Welcome the player
    clear()
    height, width = welcome()
    print()

    # Create a heightxwidth board
    game_board = [(["□"] * width) for x in range(height)]

    # Attributes of the game
    game_round = 0
    current_piece = 0

    # Main game loop
    while not is_game_done(game_board):

        # Start new round
        game_round += 1
        print(f"______________Round: {game_round}______________")

        # Display current piece
        print("Current piece:")
        current_piece = randint(0,4)
        print_piece(current_piece)

        # Display game board
        print("Game board:")
        print_board(game_board)

        # Get player input
        x, y = get_player_input()
        game_board = update_board(game_board, height, width, x, y, current_piece)

        print(f"\n______________Round: {game_round}______________\n")

    # Game over
    print("Game over!")
    print_board(game_board)
    print(f"\nYou completed the board in {game_round} rounds!")