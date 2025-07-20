# N개의 도시, M개의 단방향 도로
# x부터 출발해서 최단 경로의 길이가 k인 도시번호 출력

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
print(graph)
# 최단 경로 -> dfs
res = []
def dfs(start, dist):
    if dist == K:
        res.append(start)
        return
    for adj in graph[start]:
        dfs(adj, dist+1)

res.sort()
if len(res):
    for v in res:
        print(v)
else:
    print(-1)
dfs(1, 0)