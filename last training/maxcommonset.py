ch1=input()
ch2=input()
m=len(ch1)
n=len(ch2)
def lcs(ch1,ch2,m,n,dp):
    if (m==0 or n==0):
        return 0
    if (dp[m][n]!=-1):
        return dp[m][n]
    if (ch1[m-1]==ch2[n-1]):
        ans=1+lcs(ch1,ch2,m-1,n-1,dp)
        dp[m][n]=ans
        return ans
    else:
        ans1=lcs(ch1,ch2,m-1,n,dp)
        ans2=lcs(ch1,ch2,m,n-1,dp)
        dp[m][n]=max(ans1,ans2)
        return max(ans1,ans2)
        
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
answ=lcs(ch1,ch2,m,n,dp)
print(answ)