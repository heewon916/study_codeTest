# 큐
from collections import deque as dq
N, K = map(int, input().split())
q = dq([i for i in range(1, N+1)])
print("<", end='')
while q:
    for i in range(K-1):
        q.append(q.popleft())
    if len(q) > 1:
        print(q.popleft(), end=', ')
    else:
        print(q.popleft(), end='')
print(">", end=' ')