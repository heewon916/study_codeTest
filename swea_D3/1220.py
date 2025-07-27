import sys
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep1220_input.txt", "r")
from collections import deque

T = 10
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for j in range(N): # 열 별로 알아볼거야
        q = deque()
        for i in range(N):
            if graph[i][j] != 0:
                q.append(graph[i][j])
        flag = 0
        for val in q:
            if val == 1 and flag == 0:
                flag = 1
            if val == 2 and flag == 1:
                result += 1
                flag = 0
    print("#{} {}".format(tc, result))
    # while q:
    #     if q[0] == 2:
    #         q.popleft()
    #     elif q[-1] == 1:
    #         q.pop()
    #     elif q[0] == 1 and q[-1] == 2:
    #         break
    # cnt = 0
    # now = q.popleft()
    # while q:
    #     x = q.popleft()
    #     if now != x:
    #         cnt += 1
    #         now = q.popleft()

