from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 바이러스가 퍼질 수 없는 곳의 개수 최댓값
# 2가 바이러스 있는 곳: 2개 ~ 10개
# 바이러스는 상하좌우로 퍼질 수 있다. 벽을 만나면 멈춘다.
# 새로 세울 수 있는 벽의 개수는 3개 뿐이다.
# 2 중심으로 인접한 구역에서 bfs로 0인 곳을 찾아 나간다.
# 그때 0인 곳에 벽을 세우면 되지 않을까..?
###################
# 1. 벽을 세울 수 있는 곳의 개수를 센다.
#
# 2. 벽을 3개씩 세우는 모든 경우(brute force)를 BFS(너비 우선 탐색)를 돌립니다.
#
# 3. 그 중 가장 큰 값을 결과로 내놓습니다.
############


# 상 하 좌 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
#### 아이디어
# 1. 벽을 세울 수 있는 모든 경우의 수에 대해서
# 2. 바이러스가 그때마다 퍼졌을 때 0의 개수가 더 많은지 체크하기
answer = 0
def bfs():
    q = deque()
    tmp_g = deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_g[i][j] == 2:  # 2인 곳은 전부 넣어
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if tmp_g[nx][ny] == 0:
                    tmp_g[nx][ny] = 2
                    q.append((nx, ny))

    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp_g[i][j] == 0:
                cnt += 1
        # cnt += tmp_g[i].count(0)
    answer = max(answer, cnt)

def build_wall(count):
    if count == 3: #벽을 3개 다 세웠으면
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                build_wall(count+1) # 벽 세워보고 테스트
                # 3개 다 세운 경우에는 그 지점 벽 허물어야 해
                ########################
                ## 백 트래킹 지점 
                graph[i][j] = 0
build_wall(0)
print(answer)
