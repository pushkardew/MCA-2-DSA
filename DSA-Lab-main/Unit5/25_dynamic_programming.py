def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def knapsack_dp(capacity, weights, values, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]

print("Fibonacci using Dynamic Programming:")
for i in range(10):
    print(f"  F({i}) = {fibonacci_dp(i)}")

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
n = len(weights)

max_value = knapsack_dp(capacity, weights, values, n)
print(f"\n0/1 Knapsack Problem:")
print(f"  Weights: {weights}")
print(f"  Values:  {values}")
print(f"  Capacity: {capacity}")
print(f"  Maximum Value: {max_value}")
