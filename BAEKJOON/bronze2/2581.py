import math 
m = int(input())
n = int(input())

total = 0 
# li = [] 
isMin = 0 
for i in range(m, n+1):
    flag = True 
    if i>1: 
        for j in range(2, int(math.sqrt(i))+1):
            if i%j == 0: 
                flag = False
                break 
        if flag:
            total += i 
            if isMin == 0: isMin = i
            # li.append(i)
            
# if len(li) < 1: 
if total == 0 or total == 1:
    print(-1)
else: 
    print(total)
    # print(min(li))
    print(isMin)