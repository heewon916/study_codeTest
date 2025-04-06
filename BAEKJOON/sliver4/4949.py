import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == ".": break
    stk = []
    flag = True
    for c in string:
        if c == "(" or c == "[": stk.append(c)
        elif c == ")" or c == "]":
            if len(stk) == 0:
                flag = False
                break
            else:
                v = stk.pop(-1)
                if c == ")" and v != "(":
                    flag = False
                    break
                if c == "]" and v != "[":
                    flag = False
                    break
    if len(stk): flag = False
    if flag: print("yes")
    else: print("no")
