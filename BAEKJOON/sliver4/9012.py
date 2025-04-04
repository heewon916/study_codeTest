for _ in range(int(input())):
    vps = input()
    stk = []
    flag = True
    for i in range(len(vps)):
        if vps[i] == "(": stk.append(vps[i])
        else:
            if len(stk) == 0:
                # ) 로 시작하는 경우/
               flag = False
               break
            else:
                stk.pop(-1)
    if len(stk):
        # 모두 짝 찾았는데도 남는 경우
        flag = False
    if flag: print('YES')
    else: print("NO")
