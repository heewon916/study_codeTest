# 4mb = 4 * 1024 * 1024 byte = 4 * 10^6
from collections import deque as dq
N = int(input())
q = dq([(i,v) for i, v in enumerate(map(int, input().split()))])
i, move = q.popleft()
print(i+1, end=' ')
while q:
    if move > 0:
        for _ in range(move-1):
            q.append(q.popleft())
    else:
        for _ in range(abs(move)):
            q.appendleft(q.pop()
    i, move = q.popleft()
    print(i + 1, end=' ')