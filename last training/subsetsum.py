n=int(input())
ar=list(map(int,input().split()))
sum= int(input())
def subset_sum(n,ar,sum,dp):
    if sum==0:
        return 1
    if n<=0:
        return 0
    if (dp[n][sum]!=-1):
        return dp[n][sum]
    if(ar[n-1]>sum):
        dp[n][sum]=subset_sum(n-1,ar,sum,dp)
        return dp[n][sum]
    else:
        pick=subset_sum(n-1,ar,sum-ar[n-1],dp)
        notpick=subset_sum(n-1,ar,sum,dp)
        dp[n][sum]=pick or notpick
        return pick or notpick
dp = [[-1 for i in range(sum+1)] for j in range(n+1)]
print(subset_sum(n,ar,sum, dp))