N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

## !!! 정점 번호가 작은 것부터 방문하고 싶다고 했으므로.
for adj in graph:
    adj.sort()

def bfs(v):
    visited = [0] * (N + 1)
    q = [v]
    visited[v] = 1
    while q:
        x = q.pop(0)
        # visited[x] = 1 # 노드를 꺼낼 때 처리하면 같은 노드가 중복해서 큐에 들어갈 수 있음.
        print(x, end=' ')
        for z in graph[x]:
            if not visited[z]:
                q.append(z)
                visited[z] = 1

visited = [0] * (N+1)
def dfs(v):
    global visited
    visited[v] = 1
    print(v, end=' ')
    for z in graph[v]:
        if not visited[z]:
            dfs(z)

dfs(V)
print()
bfs(V)