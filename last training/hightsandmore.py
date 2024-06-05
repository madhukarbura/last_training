#given an arry of integers find the highest and second highest and lowest of the given one
#given an arry check if it is following arthematic progression or not (12345)
arr=list(map(int,input().split()))
arr.sort()
print("highest number=",arr[-1],"\n""second highest number",arr[-2],"\n""smallest or lowest",arr[0])
