fly = []
while True:
    pair = input()
    if pair == "":
        break
    x,y = map(int, pair.split(','))
    fly.append([x,y])
diff=[]
sum = 0
for i in range(0,len(fly)):
    sum += fly[i][0]
    diff.append(fly[i][1]-fly[i][0])
diff.sort()
for i in range(0,len(fly)//2):
    sum += diff[i]
print(sum)