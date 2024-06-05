"""n=list(map(int,input().split()))
m=list(map(int,input().split()))
k=[]
for i in range(len(n)):
    for j in range(len(m)):
        k.append(n[i]^m[j])
h=0
for i in range(len(k)):
    h=h^k[i]
print(h)"""

#optimized o(n)

# nums1 = list(map(int, input().split()))
# nums2 = list(map(int, input().split()))
# nums3 = []
# for i in nums1:
#     for j in nums2:
#         nums3.append(i^j)
# res = 0
# for i in nums3:
#     res = res ^ i
# print(res)
'''Optimized'''
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
m = len(nums1)
n = len(nums2)
val = 0
if m % 2 == 0 and n % 2 == 0:
    print(0)
elif m % 2 == 0:
    for i in nums1:
        val = val ^ i
    print(val)
elif n % 2 == 0:
    for i in nums2:
        val = val ^ i
    print(val)
else:
    for i in nums1:
        val = val ^ i
    for i in nums2:
        val = val ^ i
    print(val)