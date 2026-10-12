
# Map Colouring using CSP

n = int(input("Enter number of regions: "))

regions = []
for i in range(n):
    regions.append(input("Enter region name: "))

colours = input("Enter colours separated by space: ").split()

graph = {region: [] for region in regions}

e = int(input("Enter number of adjacent region pairs: "))

for i in range(e):
    a, b = input("Enter adjacent regions: ").split()
    graph[a].append(b)
    graph[b].append(a)

assigned = {}

def solve():
    if len(assigned) == n:
        return True

    for region in regions:
        if region not in assigned:
            for colour in colours:
                valid = True

                for neighbour in graph[region]:
                    if assigned.get(neighbour) == colour:
                        valid = False
                        break

                if valid:
                    assigned[region] = colour

                    if solve():
                        return True

                    del assigned[region]

            return False

    return True

if solve():
    print("\nMap Colouring Solution:")
    for region, colour in assigned.items():
        print(region, ":", colour)
else:
    print("No valid colouring possible")
