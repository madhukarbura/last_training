def houserob(nums, n, dp):
    if n <= 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    pick = nums[n-1] + houserob(nums, n-2, dp)
    notpick = 0 + houserob(nums, n-1, dp)
    dp[n] = max(pick, notpick)
    return max(pick,notpick)
nums = list(map(int, input().split()))
n = len(nums)
dp = [-1 for i in range(n+1)]
print(houserob(nums, n, dp))