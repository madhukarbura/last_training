n=int(input("enter the length:"))
profit=list(map(int,input("enter the profits:").split()))
weight=list(map(int,input("enter the weight:").split()))
capacity=int(input("enter the capacity"))
def knapsack(n,profit,weight,capacity):
    if capacity==0:
        return 0
    if n==0:
        return 0
    if weight[n-1]>capacity:
        return knapsack(n-1,profit,weight,capacity)
    else:
        pick=profit[n-1]+knapsack(n-1,profit,weight,capacity-weight[n-1])
        notpick=0+knapsack(n-1,profit,weight,capacity)
        return max(pick,notpick)
    
ans=knapsack(n,profit,weight,capacity)
print(ans)