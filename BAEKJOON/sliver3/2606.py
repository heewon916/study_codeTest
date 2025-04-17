# 그래프 상에서 연결된 노드의 개수
# 전체 탐색 필요: dfs

def dfs(start, N):
    global visited
    for i in range(N+1):
        if graph[start][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(i, N)
N = int(input())
M = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
visited = [0] * (N+1)
visited[1] = 1
dfs(1, N)
# print(visited)
print(sum(visited)-1)