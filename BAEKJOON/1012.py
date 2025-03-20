# 네트워크 개수
# 상하좌우
# dfs 로 가볼게
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())
dn = [0, 1, 0, -1]
dm = [1, 0, -1, 0]
def dfs(pt, graph, visited):
    n1, m1 = pt
    visited[n1][m1] = 1
    for i in range(4):
        n2, m2 = n1+dn[i], m1+dm[i]
        if 0<=n2<n and 0<=m2<m:
            if graph[n2][m2] == 1 and not visited[n2][m2]:
                visited[n2][m2] = 1
                dfs((n2,m2), graph, visited)

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        mi, ni = map(int, input().split())
        graph[ni][mi] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for ni in range(n):
        for mj in range(m):
            if graph[ni][mj] == 1 and not visited[ni][mj]:
                dfs((ni,mj), graph, visited)
                cnt += 1

    print(cnt)