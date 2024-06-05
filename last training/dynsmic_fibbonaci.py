def fibb(n,dp):
    if n==1:
        dp[1]=0
        return 0
    if n==2:
        dp[2]=1
        return 1
    if dp[n]!=-1:
        return dp[n]
    ans= fibb(n-1,dp)+fibb(n-2,dp)
    dp[n]=ans
    return ans
n=int(input("enter the number: "))
dp=[]
for i in range(0,n+1):
    dp.append(-1)
ans=fibb(n,dp)
print(ans)