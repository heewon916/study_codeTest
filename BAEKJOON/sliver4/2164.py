from collections import deque as dq
import sys
input = sys.stdin.readline
N = int(input())
q = dq([i for i in range(1, N+1)])

while len(q)>1:
    q.popleft()
    v = q.popleft()
    q.append(v)
print(q[0])