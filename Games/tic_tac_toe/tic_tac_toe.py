# Tic-Tac-Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    for i in range(0, 9, 3):
        print('|', board[i], '|', board[i+1], '|', board[i+2], '|')
        print('-------------')

# Function to make a move
def make_move(player, position):
    board[position] = player

# Function to check for a win
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if all(board[i+j] == player for j in range(3)):
            return True

    # Check columns
    for i in range(3):
        if all(board[i+j] == player for j in range(0, 7, 3)):
            return True

    # Check diagonals
    if all(board[i] == player for i in range(0, 9, 4)) or all(board[i] == player for i in range(2, 7, 2)):
        return True

    return False

# Function to check for a draw
def check_draw():
    return ' ' not in board

# Function to play the game
def play_game():
    current_player = 'X'

    while True:
        display_board()

        # Get player's move
        move = input(f"Player {current_player}, make your move (0-8): ")
        move = int(move)

        # Make the move
        if 0 <= move <= 8 and board[move] == ' ':
            make_move(current_player, move)
        else:
            print("Invalid move. Try again.")
            continue

        # Check for a win
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw():
            display_board()
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
