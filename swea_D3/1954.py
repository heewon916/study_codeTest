T = int(input())
def snail(x, y, cnt, dr):
    graph[x][y] = cnt
    nx = x + dx[dr]
    ny = y + dy[dr]
    if cnt == N*N:
        return
    if nx<0 or ny<0 or nx>=N or ny>=N or graph[nx][ny] != 0:
        dr = (dr+1) % 4
        snail(x, y, dr, cnt)
    else:
        snail(nx, ny, dr, cnt+1)
for tc in range(1, T+1):
    N = int(input())
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    graph = [[0 for _ in range(N)] for _ in range(N)]
    snail(0, 0, 1, 0)

    for i in graph:
        print(i)
