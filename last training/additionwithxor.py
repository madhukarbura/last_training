x=int(input())
y=int(input())
while(y!=0):
    ans =x^y
    carry=x&y
    carry=carry<<1
    y=carry
    x=ans
print(x)