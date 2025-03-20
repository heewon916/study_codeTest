M, N, H = map(int, input().split())
# M 가로 N 세로 H 높이 
matrix = []

for h in range(H):
    tmp = []
    for n in range(N):
       tmp.append(list(map(int, input().split())))
    matrix.append(tmp)
        
# for h in range(H):
#     print(matrix[h])
# matrix[0] => 0층에 있는 mxn 크기의 상자 
# matrix[0][1][1] => 0층에 있는 상자의 2번째 줄(n=2)에서 2번째 토마토(m=2)
# matrix[h][n][m] = matrix[x][y][z]
# 상하좌우앞뒤 순서 
dh = [1, -1, 0, 0, 0, 0] 
dn = [0, 0, 0, 0, -1, 1] 
dm = [0, 0, -1, 1, 0, 0] 

# 상하좌우앞뒤에 1인 게 있으면 0은 1일 뒤에 1으로 변경된다. 
# 한 층마다 전체를 살펴야 하지만, 최소일수 구하기니까 BFS가 맞다 
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
q = [] 
# 각 층의 익은 토마토 기준으로 주변을 전부 방문했다고 하고 
def bfs():
    while q:
        h, n, m = q.pop(0)
        visited[h][n][m] = 1
        for i in range(6):
            nh, nn, nm = h+dh[i], n+dn[i], m+dm[i]
            if 2<=nm <=100 and 2<=nn<=100 and 1<=nh<=100: # 범위 안에 있을 때
                if matrix[nh][nn][nm] == 0 and visited[nh][nn][nm] == 0: # 익지 않은 토마토고, 아직 방문 안했으면
                    q.append(nh, nn, nm)
                    visited[nh][nn][nm] = 1
                    matrix[nh][nn][nm] = 1
for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix[h][n][m] == 1: # 익은 경우에 대해서만 dfs 시행하기 
                q.append((h, n, m))
                bfs() 

# 날짜 확인을 어떻게 하지