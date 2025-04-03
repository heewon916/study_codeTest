T = int(input())

for tc in range(T):
    stack = [] # ) 만 저장
    vps = input()
    flag = 1
    for v in vps:
        if v == "(":
            stack.append(v)
        elif v == ")":
            if stack:
                stack.pop()
            else:
                flag = 0
                break
    if stack or flag == 0 :
        print("NO")
    else:
        print("YES")










