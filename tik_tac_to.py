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
