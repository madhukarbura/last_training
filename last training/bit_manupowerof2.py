def bit_power_of_2(n):
    if n<=0:
        return False
    return  n & n-1 ==0
        
            
        
n=int(input())
result=bit_power_of_2(n)
print(result)
"""16
10000
01111
&=0000"""