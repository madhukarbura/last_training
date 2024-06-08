n=int(input())
m=bin(n)
k=str(m)
count=0
for i in range(len(k)):
    if k[i]=="1":
        count+=1
print(count)

    