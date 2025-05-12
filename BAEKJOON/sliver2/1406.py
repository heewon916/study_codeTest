import sys
from collections import deque
input = sys.stdin.readline

leftQ = deque(list(map(str, input().rstrip())))
rightQ = deque()
# string = list(map(str, input().rstrip()))
M = int(input().rstrip())
# cursor = len(string)

for _ in range(M):
    cmd = input().rstrip()
    if cmd == "L":
        if leftQ:
            rightQ.appendleft(leftQ.pop())
    elif cmd == "D":
        if rightQ:
            leftQ.append(rightQ.popleft())
    elif cmd == "B":
        if leftQ: leftQ.pop()
    else:
        cmd0, cmd1 = cmd.split()
        leftQ.append(cmd1)
print(''.join(leftQ + rightQ))