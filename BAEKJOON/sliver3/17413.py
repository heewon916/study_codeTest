import sys
import re
input = sys.stdin.readline

s = input().rstrip()
# 공백으로 나눠서 각 단어를 확인
# 각 단어에서 <를 만나면 >를 만날 때까지 쭉 출력
tmp = ''
flag = False
for i in range(len(s)):
    if s[i] == "<":
        flag = True
        tmp =''
    elif s[i] == ">":
        flag = False
        print(s[i], end='')
        continue
    # 만약 <> 안에 있는 문자라면
    if flag:
        print(s[i], end='')
    # <> 밖에 있는 문자라면
    else:
        # 만약 다음 문자가 공백이 있으면 출력 후, tmp 초기화
        if s[i] == " ":
            print(s[i], end='')
        else:
            tmp += s[i]
        if i < len(s)-1:
            if s[i+1] == " " or s[i+1] == "<":
                print(''.join(tmp[::-1]), end='')
                tmp = ''
        else:
            print(''.join(tmp[::-1]), end='')
# >가 끝나면 <가 나올 때까지 해당 단어 임시 저장 후 반대로 뒤집어 출력
