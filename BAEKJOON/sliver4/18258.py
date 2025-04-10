from collections import deque as dq
import sys
input = sys.stdin.readline

N = int(input())
q = dq([])
for _ in range(N):
    cmd = input().rstrip().split()
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
        print(q[0] if len(q) else -1)
    elif cmd[0] == "back":
        print(q[-1] if len(q) else -1)