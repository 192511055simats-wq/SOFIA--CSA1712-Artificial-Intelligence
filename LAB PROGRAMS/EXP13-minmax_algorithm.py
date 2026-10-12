def minimax(board, depth, is_max):
    if "X" in board and board.count("X") == 3:
        return 1
    if "O" in board and board.count("O") == 3:
        return -1
    if " " not in board:
        return 0
    if is_max:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, depth + 1, False))
                board[i] = " "
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, depth + 1, True))
                board[i] = " "
        return best

board = [" " for i in range(9)]

print("Enter 9 positions (X, O or - for empty):")
for i in range(9):
    x = input()
    board[i] = " " if x == "-" else x.upper()

best_score = -100
best_move = -1

for i in range(9):
    if board[i] == " ":
        board[i] = "X"
        score = minimax(board, 0, False)
        board[i] = " "

        if score > best_score:
            best_score = score
            best_move = i

if best_move != -1:
    print("Best move for X:", best_move + 1)
else:
    print("No moves available")
