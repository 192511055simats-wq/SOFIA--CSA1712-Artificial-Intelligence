from itertools import permutations
n = int(input("Enter number of cities: "))
print("Enter cost matrix:")
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))
cities = list(range(1, n))
min_cost = float('inf')
best_route = []
for p in permutations(cities):
    route = [0] + list(p) + [0]
    total = 0
    for i in range(len(route) - 1):
        total += cost[route[i]][route[i + 1]]
    if total < min_cost:
        min_cost = total
        best_route = route

print("Shortest route:", end=" ")
for city in best_route:
    print(city, end=" ")
print("\nMinimum cost:", min_cost)
