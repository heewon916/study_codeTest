import math 
m = int(input())
n = int(input())
li = [] 
for i in range(m, n+1):
    if math.sqrt(i) - int(math.sqrt(i)) == 0: 
        li.append(i)
if len(li)>0: 
    print(sum(li))
    print(li[0])
else:
    print(-1)