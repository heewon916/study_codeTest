from collections import deque 
INF = float('inf')
N, M = map(int, input().split()) # 양의 정수
mat = [list(map(int, input())) for _ in range(N)]
dp = [[INF] * (M) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)]
dxy = [[-1,0], [1,0], [0,-1], [0,1]]

q = deque([(0,0)])
dp[0][0] = 1 # 이걸 안해주니까 dp값이 뭘해도 INF이지 
while q: 
    x, y = q.popleft()
    visited[x][y] = 1 
    temp = []
    for move in dxy: 
        nx, ny = x+move[0], y+move[1] # 상하좌우
        if 0<=nx<N and 0<=ny<M: 
            if not visited[nx][ny] and mat[nx][ny] == 1: # 방문하지 않았고, 1인 곳을 탐색
                visited[nx][ny] = 1 
                q.append((nx, ny)) # 다음으로 방문하는 곳들
                dp[nx][ny] = min(dp[nx][ny], dp[x][y] + 1)
print(dp[N-1][M-1])