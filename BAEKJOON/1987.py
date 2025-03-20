R, C = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited_alpha = [0] * 26 # 알파벳 개수만큼만
graph = []
for i in range(R):
    graph.append(list(map(str, input())))
ans = 0
def dfs(x, y, c):
    global ans
    ans = max(ans, c)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<R and 0<=ny<C and visited_alpha[ord(graph[nx][ny])-ord('A')] == 0:
            dfs(nx, ny, c+1)

# # from collections import deque
# R, C = map(int, input().split())
# # visited = [[0]*C for _ in range(R)]
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# graph = []
# for i in range(R):
#     graph.append(list(map(str, input())))
#
# chars = ""
# # q = deque()
# # q.append((0,0))
#
# ans = 0
#
#
#
#
# # def bfs():
# #     global ans, chars
# #     while len(q):
# #         x, y = q.popleft()
# #         # visited[x][y] = 1
# #         for i in range(4):
# #             nx, ny = x+dx[i], y+dy[i]
# #             # if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
# #             #     visited[nx][ny] = 1
# #             if 0<=nx<R and 0<=ny<C and graph[nx][ny] not in chars:
# #                     print(f"chars = {chars}, new {nx},{ny} = {graph[nx][ny]}")
# #                     chars += graph[x][y]
# #                     q.append((nx, ny))
# #                     print(f"q = {q}")
# #
# # bfs()
# print(ans)