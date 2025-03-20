N = int(input()) # 컴퓨터의 수 0~100 
edges = int(input()) # 연결되어 있는 컴퓨터 쌍의 수 

# 모두 탐색해야 하는 경우니까 DFS로 가죠 

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(edges):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
    
visited = [0] * (N+1) 

def dfs(start):
    visited[start] = 1
    # for i in graph[start]:
    #     if visited[i] == 0: 
    #         dfs(i)
    for i in range(1, N+1):
        if not visited[i] and graph[start][i] == 1:
            dfs(i)
    
dfs(1)
print(sum(visited)-1)
