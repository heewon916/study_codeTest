N, M, V = map(int, input().split())
visited = [False] * (N+1)
visited2 = [False] * (N+1)
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
def dfs(start):
    visited[start] = True 
    print(start, end=" ")
    for i in range(1, N+1):
        if graph[start][i] == 1 and visited[i] == False:
            dfs(i)
    
def bfs(start):
    q = [start]
    visited2[start] = True 
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if graph[v][i] == 1 and not visited2[i]:  
                q.append(i)
                visited2[i] = True
                
dfs(V)
print()
bfs(V)