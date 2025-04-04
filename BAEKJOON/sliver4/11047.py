import sys
input = sys.stdin.readline
N, K = map(int, input().split())
li = []
for _ in range(N):
    li.append(int(input()))

li.sort(reverse=True)
res = 0
for i in range(N):
    if K == 0:
        break
    res += K//li[i]
    K %= li[i]
    # print(res, K)
print(res)