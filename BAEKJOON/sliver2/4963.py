import sys
sys.setrecursionlimit(10**6)
di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(i, j):
    global visited
    for u in range(8):
        ni, nj = i+di[u], j+dj[u]
        if 0<=ni<h and 0<=nj<w:
            if not visited[ni][nj] and graph[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj)
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # w: col, h: row
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]:
                visited[i][j] = 1
                count += 1
                dfs(i, j)
    print(count)
