import sys
sys.setrecursionlimit(10**6)

row, col = map(int,input().split())
graph = [list(map(str, input())) for _ in range(row)]
visited = [[0]*col for _ in range(row)]
# I 위치 찾기
for i in range(row):
    for j in range(col):
        if graph[i][j] == 'I':
            pos = (i, j)
            break

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0

def dfs(x, y):
    global count
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<row and 0<=ny<col:
            if graph[nx][ny] != 'X' and not visited[nx][ny]:
                if graph[nx][ny] == 'P':
                    count += 1
                dfs(nx, ny)

dfs(pos[0], pos[1])
if count == 0:
    print('TT')
else:
    print(count)



