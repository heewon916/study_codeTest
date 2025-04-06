from collections import deque as dq
import sys
input = sys.stdin.readline
q = dq([])
N = int(input())
for _ in range(N):
    cmd = input().rstrip().split()
    if cmd[0] == "push_front":
        q.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        q.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if len(q): print(q.popleft())
        else: print(-1)
    elif cmd[0] == "pop_back":
        if len(q): print(q.pop())
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
