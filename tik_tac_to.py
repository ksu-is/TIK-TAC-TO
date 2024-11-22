import random 
# Function to print the game board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
# Function to check for a winner 
def check_winner(board, player):
    #check rows, columns, and diagonals
    for row in board 
        if all(cell == player for cell in row):
            return True 
for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
# Function to check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Function for the AI's move
def ai_move(board):
    # Check for winning move or block player
    for player in ["O", "X"]:  # Prioritize AI's win (O), then block player (X)
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    if check_winner(board, player):
                        return
                    board[row][col] = " "  # Undo move
                    
# Otherwise, choose a random empty cell
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"

# Main game function
def tic_tac_toe():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to James's Tic-Tac-Toe!")
    print("You are 'X'. AI is 'O'.")
    print_board(board)
     while True:
        # Player's turn
        print("Your turn.")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                print_board(board)

                # Check for winner
                if check_winner(board, "X"):
                    print("You win! Congratulations!")
                    break

                # Check for a tie
                if is_full(board):
                    print("It's a tie!")
                    break

                # AI's turn
                print("AI's turn...")
                ai_move(board)
                print_board(board)

                # Check for winner
                if check_winner(board, "O"):
                    print("AI wins! Better luck next time.")
                    break

                # Check for a tie
                if is_full(board):
                    print("It's a tie!")
                    break
            else:
                print("Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
