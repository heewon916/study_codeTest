from collections import deque
tc = int(input())
for _ in range(tc):
    cmdline = map(str, input())
    left_stk = deque()
    right_stk = deque()
    for cmd in cmdline:
        if cmd == "<":
            if len(left_stk):
                right_stk.appendleft(left_stk.pop())
        elif cmd == ">":
            if len(right_stk):
                left_stk.append(right_stk.popleft())
        elif cmd == "-":
            if len(left_stk): left_stk.pop()
        else:
            left_stk.append(cmd)
    print(''.join(left_stk)+''.join(right_stk))



