n=int(input())
count=0
i=1
while(i<n+1):
    if n&i:
        count+=1
    i=i*2
print(count)    