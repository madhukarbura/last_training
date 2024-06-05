def count_subsets_with_sum(arr, sum,dp,n):
    
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(sum + 1):
            dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] += dp[i-1][j - arr[i-1]]
    
    
    return dp[n][sum]


arr = list(map(int,input().split()))
n = len(arr)
sum = int(input())
dp = [[0 for i in range(sum + 1)] for j in range(n + 1)]
print(count_subsets_with_sum(arr, sum,dp,n))  
