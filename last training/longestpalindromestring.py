name=input()
m=name[::-1]
n=len(name)
def lcs(ch1,ch2,m,n,):
    if (m==0 or n==0):
        return 0
    
    if (ch1[m-1]==ch2[n-1]):
        ans=1+lcs(ch1,ch2,m-1,n-1)
        
        return ans
    else:
        ans1=lcs(ch1,ch2,m-1,n)
        ans2=lcs(ch1,ch2,m,n-1)
        
        return max(ans1,ans2)
        

answ=lcs(name,m,n,n)
print(answ)