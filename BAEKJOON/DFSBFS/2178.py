N, M = map(int, input().split())
graph = []
visited = [[False]*M for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input())))
# for row in graph: 
#     print(row)
end = [N-1, M-1]
# 상x-1y 하x+1y좌xy-1우xy+1 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = []
# 상 하 좌 우로 움직였을 때, 배열을 벗어나지 않으면 
# 거기에 통로가 있는지 graph == 1 보고 맞으면 bfs 또 수행 
def bfs(x,y):
    q.append((x,y))
    # count = 0
    while q:
        x, y = q.pop(0)
        visited[x][y] = True 
        # print(f"ABOUT (x,y) = {x}, {y}")
        if end == [x,y]: 
            return graph[N-1][M-1]
            # print("END")   
            #return (count) 
        for i in range(4):
            nextX, nextY = x+dx[i], y+dy[i]
            if 0<=nextX<N and 0<=nextY<M:
                # print(f"\tABLE nextX, nextY = {nextX}, {nextY}")
                if visited[nextX][nextY]:
                    #print("\t\t\tALREADY VISITED")
                    continue
                if graph[nextX][nextY] == 1: 
                    q.append((nextX, nextY))
                    graph[nextX][nextY] = graph[x][y] + 1
                    # count += 1
                    # print(f"\t\tPOSSIBLE count = {count} q.append(({nextX}, {nextY}))")
                    
print(bfs(0, 0))