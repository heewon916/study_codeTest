N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
# 간선 개수
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N+1)
res = -1
def dfs(v, count):
    global res
    if v == B:
        res = count
        return True
    visited[v] = 1
    for adj in graph[v]:
        if not visited[adj]:
            dfs(adj, count+1)
    return False
if dfs(A, 0):
    print(-1)
else:
    print(res)