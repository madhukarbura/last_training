"""arr=list(map(int,input().split()))
arr1=[]
arr2=[]
for i in range(len(arr)-1):
    arr1.append(arr[i])
for j in range(1,len(arr),1):
    arr2.append(arr[j])
a=0
for i in range(0,len(arr1),2):
    a=a+arr[i]
b=0
for j in range(0,len(arr2),2):
    b=b+arr2[j]
n=max(a,b)

print(arr1,arr2,n)"""
def houserob(nums, n, dp):
    if n <= 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    pick = nums[n-1] + houserob(nums, n-2, dp)
    notpick = 0 + houserob(nums, n-1, dp)
    dp[n] = max(pick, notpick)
    return max(pick,notpick)
nums = list(map(int, input().split()))
n = len(nums)
dp = [-1 for i in range(n)]
dp1 = [-1 for i in range(n)]
arr1 = []
for i in range(0, len(nums)-1):
    arr1.append(nums[i])
arr2 = []
for i in range(1, len(nums)):
    arr2.append(nums[i])
ans1 = houserob(arr1, len(arr1), dp)
ans2 = houserob(arr2, len(arr2), dp1)
print(max(ans1, ans2))