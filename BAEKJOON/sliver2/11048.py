# NxM 크기의 그래프에서 최대 값 찾기
# 갈 수 있는 방향은 3가지 밖에
# visited처리해서 간 곳은 또 안 가게
# bfs로 not visited에 대해서 값 추가

N, M = map(int ,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = graph[0][0]
# 첫 행
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + graph[0][j]
# 첫 열
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + graph[i][0]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + graph[i][j]
print(dp[N-1][M-1])
#### 시간초과: bfs 풀이
# dr = [1, 0, 1]
# dc = [0, 1, 1]
#
# N, M = map(int ,input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0 for _ in range(M)] for _ in range(N)]
# visited[0][0] = 1 # (1,1)에서 시작
# max_res = 0
# def bfs(r, c, res):
#     global max_res
#     ### visited[r][c] = 1
#
#     if r == N-1 and c == M-1:
#         max_res = max(max_res, res)
#         return
#     visited[r][c] = 1
#     for i in range(3):
#         nr, nc = r + dr[i], c + dc[i]
#         if 0<=nr<N and 0<=nc<M:
#             if not visited[nr][nc]:
#                 bfs(nr, nc, res+graph[nr][nc])
#                 ### visited[nr][nc] = 0 ==> 함수 끝나고 복구되어야 함
#     visited[r][c] = 0
#     # else:
#     #     max_res = max(max_res, res)
#
# bfs(0, 0, graph[0][0])
# print(max_res)