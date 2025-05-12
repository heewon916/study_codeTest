# 레이저 '()'로 표현
# 쇠막대기 ( 와 )로 끝 표현
# 잘려진 막대기 조각 총 개수
import sys
from collections import deque
input = sys.stdin.readline

string = input().rstrip()
cnt = 0
res = 0
idx = 0

while idx < len(string):
    if string[idx:idx+2] == "()":
        res += cnt
        idx += 2
    else:
        if string[idx] == "(":
            cnt += 1
        else:
            cnt -= 1
            res += 1
        idx += 1
print(res)