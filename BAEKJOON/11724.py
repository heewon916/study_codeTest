import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, visited, i):
    visited[i] = 1
    for adj in graph[i]:
        if not visited[adj]:
            dfs(graph, visited, adj)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 그대로 저장하면, graph는 n+1까지 돌아야 해

cnt = 0
for i in range(1, n+1): # 여기도 0부터가 아니라 1부터여야 해
    if not visited[i]:
        dfs(graph, visited, i)
        cnt += 1
print(cnt)
# parent = [0]
# for i in range(1, n+1):
#     parent.append(i)
#
# def find(x):
#     if parent[x] != x:
#         # return find(parent[x])
#         parent[x] = find(parent[x])
#     return x
#
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a<b: parent[b] = a
#     else: parent[a] = b
#
# for i in range(m):
#     a, b = map(int, input().split())
#     union(a, b)
#
# print(parent)
# for _ in range(m):
#     u, v = map(int, input().split())
#     m = min(head[u], head[v])
#     head[u] = head[v] = m
#
#
# head.pop(0)
# print(len(set(head)))
