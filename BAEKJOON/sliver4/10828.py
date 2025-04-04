import sys
input = sys.stdin.readline
stk = []
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "pop":
        if len(stk): print(stk.pop(-1))
        else: print(-1)
    elif cmd[0] == "size":
        print(len(stk))
    elif cmd[0] == "empty":
        if len(stk): print(0)
        else: print(1)
    elif cmd[0] == "top":
        if len(stk): print(stk[-1])
        else: print(-1)
    else:
        stk.append(int(cmd[1]))
