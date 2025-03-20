import sys
from collections import deque
input = sys.stdin.readline
t = int(input()) # 테케

for _ in range(t):
    p_s = input() # 수행할 함수
    n = int(input()) #배열 원소 개수
    arr = deque(list(input()[1:-2].split(',')))
    if n == 0:
        arr = deque()
    flag = 0
    # 아이디어: 뒤집힌 횟수가 짝수면 popleft(), 홀수면 pop()
    for p in p_s:
        if p == "R":
            flag += 1
            # arr2 = deque()
            # while arr:
            #     arr2.append(arr.pop())
            # arr = arr2
        elif p == "D":
            if len(arr) == 0:
                print("error")
                break
            else:
                if flag%2 == 0: # 짝수번 뒤집음
                    arr.popleft()
                else:
                    arr.pop()
            # if len(arr) >=1 :
            #     arr.popleft()
            # else:
            #     flag = 1
            #     break
    else:
        if flag%2 == 0:
            print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
    # if flag:
    #     print("error")
    # else:
    #     print('[',end='')
    #     while arr:
    #         if len(arr) == 1:
    #             print(arr.popleft(), end='')
    #         else:
    #             print(arr.popleft(), end=',')
    #     print(']')