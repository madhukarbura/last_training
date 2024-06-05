list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
for i in range(len(list2)):
    for j in range(len(list2)-i-1):
        if list2[j]>list2[j+1]:
            #corresponding sort to list1,list2
            list2[j],list2[j+1]=list2[j+1],list2[j]
            list1[j],list1[j+1]=list1[j+1],list1[j]
ans=1
curr_end=list2[0]
for i in range(1,len(list2)):
    if list1[i]>=curr_end:
        ans+=1
        curr_end=list2[i]
print(ans)