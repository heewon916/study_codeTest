# 네트워크 개수 구하기 
# dfs로 갑시다 
N = int(input())
mat = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
res = []
dxy = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우 

## 구현 포인트? 각 단지 내에서 개수 세기 -> 매개변수로 넘길 것이냐 지역변수를 사용할 것이냐
# 아래처럼 count를 지역변수로 선언해도 문제는 안된다.
def dfs(x,y):
    visited[x][y] = 1
    count = 1
    for i in range(4):
        nx, ny = x+dxy[i][0], y+dxy[i][1]
        if 0<=nx<N and 0<=ny<N: 
            if not visited[nx][ny] and mat[nx][ny] == 1: 
                count += dfs(nx, ny)
    return count

count = 0 
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1 and not visited[i][j]: 
            visited[i][j] = 1
            res.append(dfs(i, j))
            count += 1
print(count)
res.sort()
for c in res: 
    print(c)
            