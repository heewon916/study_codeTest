import sys
from collections import deque as dq
input = sys.stdin.readline
N = int(input())

q = dq([])

for _ in range(N):
    cmd = (input().rstrip()).split()
    if cmd[0] == "push":
        q.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(q): print(q.popleft())
        else: print(-1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        if len(q): print(0)
        else: print(1)
    elif cmd[0] == "front":
        if len(q): print(q[0])
        else: print(-1)
    elif cmd[0] == "back":
        if len(q): print(q[-1])
        else: print(-1)
