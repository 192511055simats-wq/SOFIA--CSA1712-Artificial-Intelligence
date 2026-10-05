from collections import deque

def print_puzzle(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()

def get_moves(state):
    moves = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            moves.append(tuple(new_state))

    return moves


def solve(start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for next_state in get_moves(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)

    return None


# Input
print("Enter initial state (use 0 for blank):")
start = tuple(map(int, input().split()))

print("Enter goal state:")
goal = tuple(map(int, input().split()))

# Solve
solution = solve(start, goal)

if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)

    print("\nSteps:")
    for step in solution:
        print_puzzle(step)
else:
    print("No solution found.")