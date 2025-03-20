from collections import deque
N, M = map(int, input().split())
graph = []
for i in range(N):
    tmp = list(map(int, input().split()))
    # if 2 in tmp:
    #     start = [i, tmp.index(2)]
    graph.append(tmp)

visited = [[-1 for _ in range(M)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = 0

# bfs(start[0], start[1])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            bfs(i, j)

# for i in range(N):
#     print(visited[i])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()

