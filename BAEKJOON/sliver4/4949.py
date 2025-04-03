# import sys
# INPUT = sys.stdin.readline
while True:
    string = input()
    flag = 1
    if string == ".":
        break
    stk = []
    for s in string:
        if s in "([":
            stk.append(s)
        elif s == ")":
            if stk:
                top = stk.pop()
                if top != "(":
                    flag = 0
                    break
            else:
                flag = 0
                break
        elif s == "]":
            if stk:
                if stk.pop() != "[":
                    flag = 0
                    break
            else:
                flag = 0
                break

    if stk or flag == 0:
        print("no")
    else:
        print("yes")
