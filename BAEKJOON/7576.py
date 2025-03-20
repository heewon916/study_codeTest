from collections import deque
col, row = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
# visited = [[0]*col for _ in range(row)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
# pos = (-1, -1)
for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            q.append((i, j)) # 처음에 받은 토마토 중 1인 위치 모두 추가해놓기
            # 하루에 1인 토마토 주변은 동시 다발적으로 익기 때문이다.
            # break 
# q.append(pos)
#day = 0
def bfs():
    # global day
    while q:
        x, y = q.popleft()
        # visited[x][y] = 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<row and 0<=ny<col:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1 # 익는 날짜들을 더해주자.
                    q.append((nx, ny))
                # elif graph[nx][ny] == -1:
                #     continue
        #day += 1

bfs()
res = 0
# for r in graph:
#     for t in r:
#         if t == 0:
#             print(-1)
#             exit(0)
#     res = max(res, max(r))
for i in range(row):
    for j in range(col):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
    res = max(res, max(graph[i]))

# 처음에 1로 시작해 더해 나갔으니까, 1을 빼준다.
print(res-1)