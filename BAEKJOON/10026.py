import sys
sys.setrecursionlimit(10**6)
N = int(input())
graph = [list(map(str, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

# 네트워크 탐색이랑 같은 거 아닐까 DFS로 해보자.

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                dfs(nx, ny)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 적록색약 아닌 경우
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

# 적록색약인 경우
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            cnt1 += 1
print(cnt, cnt1)