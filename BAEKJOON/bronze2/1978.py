import math
ans = 0
n=int(input())
li = map(int, input().split())
for j in li:
    if j == 1:
        continue
    flag=True
    for k in range(2,int(math.sqrt(j))+1):
        if j%k==0:
            flag=False
            break
    if flag:
        ans += 1
print(ans)