import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def computer_move(board, computer_char, user_char):
    # Check if computer can win in next move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = computer_char
                if check_winner(board, computer_char):
                    return
                board[i][j] = " "

    # Check if user can win in next move and block
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = user_char
                if check_winner(board, user_char):
                    board[i][j] = computer_char
                    return
                board[i][j] = " "

    # Otherwise, make a random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = computer_char
            return

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    user_char = input("Choose your character (X or O): ").upper()
    if user_char not in ["X", "O"]:
        print("Invalid choice. Defaulting to X.")
        user_char = "X"
    computer_char = "O" if user_char == "X" else "X"

    print("Let's start the game!\n")
    print_board(board)

    while True:
        # User's move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
                if row < 1 or row > 3 or col < 1 or col > 3 or board[row-1][col-1] != " ":
                    print("Invalid move. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")

        board[row-1][col-1] = user_char
        print_board(board)

        if check_winner(board, user_char):
            print("Congratulations! You win!")
            break

        if all(cell != " " for row in board for cell in row):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's move:")
        computer_move(board, computer_char, user_char)
        print_board(board)

        if check_winner(board, computer_char):
            print("Computer wins!")
            break

        if all(cell != " " for row in board for cell in row):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
