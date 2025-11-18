def print_board(board):
    for r, row in enumerate(board):
        print(" | ".join(row))
        if r < 2:
            print("-" * 9)

def check_winner(board, player):
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

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def ai_first_available_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return (row, col)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are X, AI is O (first available moves).")
    print_board(board)

    while True:
        print("\nYour turn (X)")
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("❌ Invalid input, numbers only!")
            continue

        if (row not in [0,1,2]) or (col not in [0,1,2]) or board[row][col] != " ":
            print("❌ Invalid move, try again.")
            continue

        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("\nYou win!")
            break
        if is_full(board):
            print("\nIt's a draw!")
            break

        print("\nAI's turn (O)...")
        move = ai_first_available_move(board)
        board[move[0]][move[1]] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("\n💻 AI wins!")
            break
        if is_full(board):
            print("\n🤝 It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()