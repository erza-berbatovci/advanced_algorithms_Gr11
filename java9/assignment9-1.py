weights = [3, 2, 4, 5, 1, 6, 3, 2, 4, 1]
values  = [25, 20, 40, 50, 15, 60, 30, 22, 35, 12]
capacity = 15
n = len(weights)

dp = [[0 for w in range(capacity+1)] for i in range(n+1)]

for i in range(1, n+1):
    for w in range(1, capacity+1):
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
        else:
            dp[i][w] = dp[i-1][w]

print("Vlera maksimale e mundshme:", dp[n][capacity])

w = capacity
selected_items = []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected_items.append(i)
        w -= weights[i-1]

selected_items.reverse()
print("Objektet e zgjedhura:", selected_items)
