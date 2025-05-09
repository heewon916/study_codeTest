from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
# graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    # graph[u][v] = 1
    # graph[v][u] = 1
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        # x = q.pop(0)
        x = q.popleft()
        for adj in graph[x]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = 1

count = 0
for i in range(1,N+1):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)
