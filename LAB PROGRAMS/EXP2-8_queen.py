N = 8

board = [["." for _ in range(N)] for _ in range(N)]


def is_safe(row, col):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve(row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = "Q"

            if solve(row + 1):
                return True

            board[row][col] = "."

    return False


if solve(0):
    print("8 Queens Solution:")
    for row in board:
        print(" ".join(row))
else:
    print("No solution found")