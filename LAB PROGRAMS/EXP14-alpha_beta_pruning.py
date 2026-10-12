def alphabeta(depth, node, maximizing, values, alpha, beta):
    if depth == 3:
        return values[node]
    if maximizing:
        best = -1000
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            val = alphabeta(depth + 1, node * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = list(map(int, input("Enter 8 leaf node values: ").split()))
result = alphabeta(0, 0, True, values, -1000, 1000)
print("Optimal value:", result)
