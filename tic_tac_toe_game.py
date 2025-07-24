# Tic Tac Toe Game in Python (Terminal Version)

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows, columns and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row,col): ")
            row, col = map(int, move.split(","))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Enter row and column as 0, 1, or 2.")
        except:
            print("Invalid format. Please enter as row,col (e.g., 1,2).")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player)
        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Try again.")

def main():
    while True:
        play_game()
        choice = input("Play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
