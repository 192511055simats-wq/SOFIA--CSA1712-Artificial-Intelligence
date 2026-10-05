from collections import deque

def water_jug(jug1, jug2, target):

    queue = deque()
    queue.append((0, 0))

    visited = set()
    visited.add((0, 0))

    parent = {}
    action = {}

    while queue:

        a, b = queue.popleft()

        if a == target or b == target:

            path = []

            while (a, b) != (0, 0):
                path.append((action[(a, b)], (a, b)))
                a, b = parent[(a, b)]

            path.reverse()

            print("\nSolution:")
            print("(0, 0)")

            for step, state in path:
                print(step, "->", state)

            return

        states = [
            ((jug1, b), "Fill Jug 1"),
            ((a, jug2), "Fill Jug 2"),
            ((0, b), "Empty Jug 1"),
            ((a, 0), "Empty Jug 2")
        ]

        # Pour Jug 1 into Jug 2
        amount = min(a, jug2 - b)
        states.append(((a - amount, b + amount),
                       "Pour Jug 1 into Jug 2"))

        # Pour Jug 2 into Jug 1
        amount = min(b, jug1 - a)
        states.append(((a + amount, b - amount),
                       "Pour Jug 2 into Jug 1"))

        for state, operation in states:

            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state] = (a, b)
                action[state] = operation

    print("No solution")


# User input
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

water_jug(jug1, jug2, target)