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
