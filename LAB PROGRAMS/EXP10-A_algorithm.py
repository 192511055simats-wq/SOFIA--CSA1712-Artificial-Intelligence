graph = {}
h = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    h[node] = int(input("Enter heuristic value: "))
    graph[node] = []
e = int(input("Enter number of edges: "))
for i in range(e):
    u, v, cost = input("Enter edge (node1 node2 cost): ").split()
    cost = int(cost)
    graph[u].append((v, cost))
    graph[v].append((u, cost))
start = input("Enter start node: ")
goal = input("Enter goal node: ")
open_list = [(h[start], 0, start, [start])]
visited = set()
while open_list:
    open_list.sort()
    f, g, node, path = open_list.pop(0)
    if node == goal:
        print("Shortest path:", path)
        print("Total cost:", g)
        break
    if node not in visited:
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                open_list.append((new_f, new_g, neighbor, path + [neighbor]))
else:
    print("No path found")
