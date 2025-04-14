T = int(input())
for ts in range(T):
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(M):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1

    # 결국 최단 경로 길이를 구해야 한다.
    length = 0
    visited = [0] * N
    visited[0] = 1
    q = [0]
    while q:
        v = q.pop(0)
        for u in range(N):
            if graph[v][u] == 1 and not visited[u]:
                q.append(u)
                visited[u] = 1
                length += 1
    print(length)

        # for i in range(N):
        #     if graph[v][i] == 1 and not visited[i]:
        #         q.append(i)

    # min_l = 0
    # for start in range(N):
    #     q = [start]
    #     visited = [0] * N
    #     print(bfs(stk, visited))
    #     # min_l = min(, min_l)
    # print(min_l)
