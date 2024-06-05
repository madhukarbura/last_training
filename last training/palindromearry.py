n=int(input())
ar=list(map(int,input().split()))
flag=0
for i in range(n//2):
    if ar[i]==ar[n-i-1]:
        flag=1
if flag==1:
    print("palindrome")
else:
    print("not a palindrom")
