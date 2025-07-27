import sys
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep4615_input.txt", "r")

# 시계방향 대각선 포함
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(a, b, turn, d):     # 바꿔야 할 좌표를 willchange리스트에 넣는다
    global flag
    na = a + dx[d]
    nb = b + dy[d]
    if 0<=na<n and 0<=nb<n:
        if graph[na][nb] == turn: #turn과 같은 색을 만났다 == 그 사이에 있는 다른 색들 turn으로 바꾸기
            flag = True
            return
        if graph[na][nb] != 0 and graph[na][nb] != turn:
            willchange.append((na, nb))
            dfs(na, nb, turn, d) # 같은 방향으로 계속 보는 거야
T = int(input())
for tc in range(1, T+1):
    b, w = 0, 0
    # nxn 크기의 보드에다가 놓기
    n, m = map(int, input().split())
    # 기본 위치에 흑 백 두기
    graph = [[0 for _ in range(n)] for _ in range(n)]
    half = n//2
    # 백
    graph[half-1][half-1] = 2
    graph[half][half] = 2
    # 흑
    graph[half][half-1] = 1
    graph[half-1][half] = 1
    for _ in range(m):
        # (x,y)에 turn(1이면 흑, 2면 백) 놓기
        y, x, turn = map(int, input().split())
        graph[x-1][y-1] = turn
        for k in range(8):  # 방금 놓은 돌을 기준으로 상하좌우 대각선 살피기
            flag = False     # 그 방향에 같은 색의 컬러가 있는지 확인해야 해
            willchange = [] # 색깔이 바뀌어야 하는 좌표 리스트
            dfs(x-1, y-1, turn, k)
            if flag:    # 바꿀 수 있단 뜻
                for t in willchange:
                    graph[t[0]][t[1]] = turn
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                b += 1
            elif graph[i][j] == 2:
                w += 1
    print("#{} {} {}".format(tc, b,w))

