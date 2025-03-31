import math 
N = int(input())
li = [int(input()) for _ in range(N)] 

res = 0
for i in range(1, N):
    res += abs(li[0]-li[i])

if len(li) == 1:
    print(0)
else: 
    print(math.ceil(res/(N-1))+1)