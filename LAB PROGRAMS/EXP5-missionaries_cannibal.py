from collections import deque

m = int(input("Enter number of missionaries: "))
c = int(input("Enter number of cannibals: "))

start = (m, c, 0)
goal = (0, 0, 1)

queue = deque([start])
visited = {start}
parent = {start: None}

moves = [
    (1, 0),
    (2, 0),
    (0, 1),
    (0, 2),
    (1, 1)
]

def valid(m_left, c_left):
    m_right = m - m_left
    c_right = c - c_left

    if m_left < 0 or c_left < 0:
        return False

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


while queue:

    current = queue.popleft()
    ml, cl, boat = current

    if current == goal:
        path = []

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        print("\nSolution:")
        for state in path:
            print(state)

        break

    for dm, dc in moves:

        if boat == 0:
            new_state = (ml - dm, cl - dc, 1)
        else:
            new_state = (ml + dm, cl + dc, 0)

        if new_state not in visited:
            if valid(new_state[0], new_state[1]):
                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)

else:
    print("No solution")