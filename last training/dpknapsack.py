n = int(input())
profit = list(map(int, input().split()))
weight = list(map(int, input().split()))
capacity = int(input())
def knapsack(n, profit, weight, capacity, dp):
    if capacity == 0:
        return 0
    if n == 0:
        return 0
    if dp[n][capacity] != -1:
        return dp[n][capacity]
    if weight[n-1] > capacity:
        dp[n][capacity] = knapsack(n-1, profit, weight, capacity, dp)
        return dp[n][capacity]
    else:
        pick = profit[n-1] + knapsack(n-1, profit, weight, capacity-weight[n-1], dp)
        notpick = knapsack(n-1, profit, weight, capacity, dp)
        dp[n][capacity] = max(pick, notpick)
    return max(pick, notpick)
dp = [[-1 for i in range(capacity+1)] for j in range(n+1)]
print(knapsack(n,profit,weight,capacity, dp))