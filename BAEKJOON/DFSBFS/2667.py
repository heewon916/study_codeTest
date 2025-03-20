# 네트워크 개수 찾는 문제 같은데 
N = int(input()) # 지도의 크기 정사각형
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
# DFS로 찾아야 할 것 같다. 
visited = [[0]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
tmplist = [] 
def dfs(x, y):
    global count
    visited[x][y] = 1
    count += 1
    #print(f"VISIT ({x}, {y})")
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny)
answer = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == 1: 
            # 방문은 안했는데, 그래프에는 존재하면 
            answer += 1
            count = 0 
            dfs(i, j)
            tmplist.append(count)
tmplist.sort()
print(answer)
for i in tmplist:
    print(i)