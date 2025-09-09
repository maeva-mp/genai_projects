#Mini-Project - Tic Tac Toe
#Build a tic tac toe game between 2 players

#What do we know (the problem description):
#It is a 3 x 3 board game
#Players take turn ( players are expected to give an input)
#There are symbols X and O
#There are 3 outputs that have to be checked each time : win, loss or tie

print("Welcome Tic Tac Toe")

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    for i in range(3):
        print(" " + " | ".join(board[i]))
        print("---+---+---")

def player_input(player):
    print(f"Player {player}'s turn.")
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if row in range(3) and col in range(3):
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Try again.")
            else:
                print("Input numbers between 0 and 2.")
        except ValueError:
            print("Please enter numbers.")

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

board = create_board()
current_player = 'X'

while True:
    display_board(board)
    row, col = player_input(current_player)
    board[row][col] = current_player
    if check_winner(board, current_player):
        display_board(board)
        print(f"Player {current_player} wins!")
        break
    elif is_draw(board):
        display_board(board)
        print("It's a draw!")
        break
    current_player = 'O' if current_player == 'X' else 'X'
