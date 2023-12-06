import tkinter as tk
import random

class Piece:
    def __init__(self, team):
        self.team = team
        self.is_king = False
        self.row = None
        self.col = None

    def can_move_forward(self, dest_row, capture=False):
        if self.is_king:
            return True
        if capture:
            return abs(dest_row - self.row) == 2
        if self.team.color == 'black':
            return dest_row > self.row
        elif self.team.color == 'white':
            return dest_row < self.row
        return False

class Team:
    def __init__(self, color):
        self.color = color
        self.score = 0

def draw_board():
    root = tk.Tk()
    root.title("checkers")
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    team1 = Team('black')
    team2 = Team('white')

    turn_label = tk.Label(root, text="game start")
    turn_label.pack()

    team1_score_label = tk.Label(root, text="black team points: 0")
    team1_score_label.pack(side=tk.LEFT)

    team2_score_label = tk.Label(root, text="white team points: 0")
    team2_score_label.pack(side=tk.RIGHT)

    board = [[None for _ in range(8)] for _ in range(8)]

    # Game functions
    def click(event):
        nonlocal selected_piece
        col = event.x // 50
        row = event.y // 50
        piece = board[row][col]

        if selected_piece:
            if move_piece(row, col):
                selected_piece = None
                update_turn()
                redraw_board()  # Explicitly redraw the board after a move
            elif piece and piece.team.color == current_turn.color:
                # Selecting a different piece of the same team
                selected_piece = piece
                redraw_board()
            elif not piece or (piece and piece.team.color != current_turn.color):
                # Deselect the piece by clicking an empty square or selecting an opponent's piece
                selected_piece = None
                redraw_board()
        elif piece and piece.team.color == current_turn.color:
            selected_piece = piece
            redraw_board()

    def execute_move(src_row, src_col, dest_row, dest_col):
        board[src_row][src_col] = None
        selected_piece.row, selected_piece.col = dest_row, dest_col
        check_king(selected_piece)

        delta_row = dest_row - src_row
        delta_col = dest_col - src_col
        direction_row = delta_row // abs(delta_row)
        direction_col = delta_col // abs(delta_col)
        step_row, step_col = src_row + direction_row, src_col + direction_col

        while step_row != dest_row and step_col != dest_col:
            piece_at_step = board[step_row][step_col]
            if piece_at_step:
                capture_piece(step_row, step_col)
            board[step_row][step_col] = None
            step_row += direction_row
            step_col += direction_col

        board[dest_row][dest_col] = selected_piece
        redraw_board()

    def reset_game():
        root.destroy()
        draw_board()

    def check_king(piece):
        if piece.team.color == 'black' and piece.row == 7:
            piece.is_king = True
        elif piece.team.color == 'white' and piece.row == 0:
            piece.is_king = True

    def team_has_no_pieces(team):
        for row in board:
            for piece in row:
                if piece and piece.team == team:
                    return False
        return True

    def team_cannot_move(team):
        for r in range(8):
            for c in range(8):
                piece = board[r][c]
                if piece and piece.team == team:
                    for i in range(8):
                        for j in range(8):
                            if valid_move(piece, i, j):
                                return False
        return True
    
    def move_piece(row, col):
        src_row, src_col = selected_piece.row, selected_piece.col
        dest_row, dest_col = row, col
        delta_row = dest_row - src_row
        delta_col = dest_col - src_col

        # Check if the destination slot is already occupied
        if board[dest_row][dest_col] is not None:
            return False

        # Handle King moves
        if selected_piece.is_king:
            return handle_king_move(src_row, src_col, dest_row, dest_col)

        # Handle regular piece moves
        if abs(delta_row) == 1 and abs(delta_col) == 1:
            if selected_piece.can_move_forward(dest_row):
                execute_move(src_row, src_col, dest_row, dest_col)
                return True
        elif abs(delta_row) == 2 and abs(delta_col) == 2:
            mid_row = (src_row + dest_row) // 2
            mid_col = (src_col + dest_col) // 2
            if board[mid_row][mid_col] and board[mid_row][mid_col].team.color != selected_piece.team.color:
                if selected_piece.can_move_forward(dest_row, capture=True):
                    capture_piece(mid_row, mid_col)
                    execute_move(src_row, src_col, dest_row, dest_col)
                    return True
        return False

    def handle_king_move(src_row, src_col, dest_row, dest_col):
        delta_row = dest_row - src_row
        delta_col = dest_col - src_col
        
        # Ensure diagonal movement
        if abs(delta_row) != abs(delta_col):
            return False
        
        direction_row = int(delta_row / abs(delta_row))
        direction_col = int(delta_col / abs(delta_col))
        step_row, step_col = src_row + direction_row, src_col + direction_col
        captured_pieces = []

        while step_row != dest_row and step_col != dest_col:
            piece_at_step = board[step_row][step_col]
            if piece_at_step:
                if piece_at_step.team == selected_piece.team:
                    return False
                captured_pieces.append((step_row, step_col))
            step_row += direction_row
            step_col += direction_col
        
        # Capture all pieces
        for r, c in captured_pieces:
            capture_piece(r, c)
        
        # Make the move
        execute_move(src_row, src_col, dest_row, dest_col)
        return True

    def capture_piece(row, col):
        captured_piece = board[row][col]
        if captured_piece is not None:
            captured_team = captured_piece.team
            if captured_team == team1:
                team2.score += 1
                team2_score_label.config(text=f"white captures: {team2.score}")
            else:
                team1.score += 1
                team1_score_label.config(text=f"black captures: {team1.score}")
        board[row][col] = None

    def update_turn():
        nonlocal current_turn
        # Check for win conditions
        if team_has_no_pieces(current_turn) or team_cannot_move(current_turn):
            declare_winner(current_turn)
            return

        # Toggle the current turn
        current_turn = team2 if current_turn == team1 else team1
        turn_label.config(text=f"{current_turn.color.capitalize()}'s turn")

    def declare_winner(losing_team):
        winner_color = 'white' if losing_team.color == 'black' else 'black'
        winner_team = team2 if losing_team == team1 else team1
        
        # Update the score labels to reflect the final score
        team1_score_label.config(text=f"black captures: {team1.score}")
        team2_score_label.config(text=f"white captures: {team2.score}")
        
        # Declare the winner
        winner_window = tk.Toplevel(root)
        winner_window.title("game over")
        winner_label = tk.Label(winner_window, text=f"{winner_color} wins!")
        winner_label.pack(pady=20)
        
        reset_button = tk.Button(winner_window, text="play again", command=reset_game)
        reset_button.pack(pady=20)

    def redraw_board():
        canvas.delete("all")
        for row in range(8):
            for col in range(8):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50

                if (row + col) % 2 == 0:
                    square_color = 'white'
                else:
                    square_color = 'black'

                if selected_piece and selected_piece.row == row and selected_piece.col == col:
                    canvas.create_rectangle(x1, y1, x2, y2, fill='darkblue')
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill=square_color)

                piece = board[row][col]
                if piece:
                    if piece == selected_piece:
                        # Draw a red circle inside the selected piece
                        canvas.create_oval(x1 + 20, y1 + 20, x2 - 20, y2 - 20, fill='red')
                    if piece.team == team1:
                        canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=team1.color, outline='white')
                    elif piece.team == team2:
                        canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=team2.color)
                    if piece.is_king:
                        crown_color = 'white' if piece.team.color == 'black' else 'black'
                        # Draw a little crown for king pieces with the appropriate color
                        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text='♔', font=("Arial", 15), fill=crown_color)

                    # Highlight possible moves with green squares
                    if selected_piece:
                        for r in range(8):
                            for c in range(8):
                                if valid_move(selected_piece, r, c):
                                    x1 = c * 50 + 10
                                    y1 = r * 50 + 10
                                    x2 = x1 + 30
                                    y2 = y1 + 30
                                    canvas.create_rectangle(x1, y1, x2, y2, fill='green')

    def valid_move(piece, row, col):
        src_row, src_col = piece.row, piece.col
        dest_row, dest_col = row, col
        delta_row = dest_row - src_row
        delta_col = dest_col - src_col

        # If the destination slot is already occupied
        if board[dest_row][dest_col] is not None:
            return False
            
        # Check for valid king moves
        if piece.is_king and abs(delta_row) == abs(delta_col):
            direction_row = delta_row // abs(delta_row)
            direction_col = delta_col // abs(delta_col)
            step_row, step_col = src_row + direction_row, src_col + direction_col
            captured_piece = False

            while step_row != dest_row and step_col != dest_col:
                piece_at_step = board[step_row][step_col]
                if piece_at_step:
                    if captured_piece or piece_at_step.team == piece.team:
                        return False
                    captured_piece = True
                    step_row += direction_row
                    step_col += direction_col
                    break

                step_row += direction_row
                step_col += direction_col

            return step_row == dest_row and step_col == dest_col and (not captured_piece or board[step_row - direction_row][step_col - direction_col] != None)

        if abs(delta_row) == 1 and abs(delta_col) == 1:
            return piece.can_move_forward(dest_row)
        elif abs(delta_row) == 2 and abs(delta_col) == 2:
            mid_row = (src_row + dest_row) // 2
            mid_col = (src_col + dest_col) // 2
            if board[mid_row][mid_col] and board[mid_row][mid_col].team != piece.team:
                return piece.can_move_forward(dest_row, capture=True)  # add capture=True argument

        return False
    
    selected_piece = None
    random_team = [team1, team2]
    current_turn = random.choice(random_team)
    turn_label.config(text=f"match starts! its {current_turn.color} team's turn!")
    canvas.bind("<Button-1>", click)

    # Initialize the board
    for row in range(8):
        for col in range(8):
            if row < 3 and (row + col) % 2 != 0:
                board[row][col] = Piece(team1)
                board[row][col].row, board[row][col].col = row, col
            elif row > 4 and (row + col) % 2 != 0:
                board[row][col] = Piece(team2)
                board[row][col].row, board[row][col].col = row, col

    redraw_board()
    root.mainloop()

draw_board()
