from collections import deque

N = int(input())
dq = deque([x for x in range(1,N+1)])

while len(dq)>1:
    dq.popleft()
    n = dq.popleft()
    dq.append(n)
print(dq[0])