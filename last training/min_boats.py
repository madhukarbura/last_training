people=list(map(int,input().split()))
limit=int(input())
people.sort()
j=len(people)-1
i=0
min_boats=0
while i<=j:
    if people[i]+people[j]>limit:
        j-=1
    else:
        i+=1
        j-=1
    min_boats+=1
print(min_boats)