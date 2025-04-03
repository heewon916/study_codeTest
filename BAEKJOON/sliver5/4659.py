li = [chr(i) for i in range(ord('a'), ord('a')+26)]
#모음
li1 = list('a,e,i,o,u'.split(','))
#자음 
li2 = list(set(li).difference(li1))

# 모음 하나 반드시 포함
# 모음 3개 연속 불가
# 자음 3개 연속 불가
# 같은 글자 연속 2번 불가
# ee, oo 는 허용함

while True:
    pw = input()
    if pw == "end": break
    chk = [0 for _ in range(len(pw))]
    prev = ''
    cnt = 0
    flag = True
    for i in range(len(pw)):
        # 같은 글자 연속 2번 불가
        if prev != pw[i]:
            prev = pw[i]
            cnt = 1
        else:
            cnt += 1
            if cnt == 2:
                # ee, oo 는 허용함
                if prev == 'e' or prev == 'o':
                    pass
                else:
                    flag = False
                    break
        # 모음1 자음2
        if pw[i] in li1: chk[i] = 1
        elif pw[i] in li2: chk[i] = 2
    # print(pw, chk)
    # 모음 3개 연속 불가. 자음 3개 연속 불가
    if "111" in ''.join(map(str, chk)) or "222" in ''.join(map(str, chk)):
        flag = False
    # 모음 하나 반드시 포함
    if 1 not in chk:
        flag = False
    if flag:
        print("<{}> is acceptable.".format(pw))
    else:
        print("<{}> is not acceptable.".format(pw))
