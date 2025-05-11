import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

### dfs
# visited = [0] * (N+1)
# parent = [-1] * (N+1)
# parent[1] = 0
#
# def dfs(v):
#     visited[v] = 1
#     for adj in graph[v]:
#         if not visited[adj]:
#             parent[adj] = v
#             dfs(adj)
# dfs(1)
# for i in range(2, N+1):
#     print(parent[i])

### bfs
visited = [0] * (N + 1)
parent = [-1] * (N + 1)
parent[1] = 0
def bfs(v):
    q = deque([v])
    visited[1] = 1
    # prev = 1
    while q:
        x = q.popleft()
        for adj in graph[x]:
            if not visited[adj]:
                q.append(adj)
                parent[adj] = x
                visited[adj] = 1
        # prev = x
bfs(1)
for i in range(2, N+1):
    print(parent[i])