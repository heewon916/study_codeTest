import math 
N = int(input())
li = [int(input()) for _ in range(N)] 
v = li.pop(0)
cnt = 0 
li.sort(reverse=True)
if len(li)>0:
    while v <= li[0]:
        li[0] -= 1
        v += 1
        cnt += 1
        li.sort(reverse=True)
    print(cnt)
    # print(v, li)
else: 
    print(0)
# res = 0
# for i in range(1, N):
#     res += abs(li[0]-li[i])

# if len(li) == 1:
#     print(0)
# else: 
#     print(math.ceil(res/(N-1))+1)