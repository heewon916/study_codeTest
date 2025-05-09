# 서로 인접한 배추가 몇 군데? => 그래프 개수 몇개?
### 1. 재귀 깊이 제한
# import sys
# sys.setrecursionlimit(10**6)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # dfs 활용
    def dfs(i, j):
        visited[i][j] = 1
        for m in range(4):
            ni, nj = i + dx[m], j + dy[m]
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and graph[ni][nj] == 1:
                    dfs(ni, nj)
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if not visited[i][j]:
                    count += 1
                    dfs(i, j)
    print(count)

    ### 2. 반복 dfs
    # dx = [1, -1, 0, 0]
    # dy = [0, 0, 1, -1]
    # stack = []
    # # dfs 활용
    # def dfs(i, j):
    #     stack = [(i, j)]
    #     visited[i][j] = 1
    #     while stack:
    #         x, y = stack.pop()
    #         for m in range(4):
    #             ni, nj = x+dx[m], y+dy[m]
    #             if 0<=ni<N and 0<=nj<M:
    #                 if not visited[ni][nj] and graph[ni][nj] == 1:
    #                     # dfs(ni, nj)
    #                     stack.append((ni, nj))
    #                     visited[ni][nj] = 1
    # count = 0
    # for i in range(N):
    #     for j in range(M):
    #         if graph[i][j] == 1:
    #             if not visited[i][j]:
    #                 count += 1
    #                 dfs(i, j)
    # print(count)