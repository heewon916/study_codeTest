# 최소 몇 번을 눌러야 하는지이다. BFS 해당 
F, S, G, U, D = map(int, input().split())
# G층에 가야하고, S층에 현재 있음
# 위로 U, 아래로 D 최대 F층까지 있음

q = [] 
visited = [0 for _ in range(F+1)]
answer = 0
def bfs(s):
    global answer
    q.append(s)
    while q:
        v = q.pop(0)
        if v == G: 
            return visited[v]
        for nv in [v+U, v-D]:
            if 1<=nv<=F and not visited[nv] and nv != s: # 포인트: 만약, u,d가 0이라서 nv가 원래 위치일때는 고려할 이유가 X
                q.append(nv)
                visited[nv] = visited[v] + 1
                #print(f"\tAPPEND {nv} button={visited[nv]}")
    return "use the stairs"
print(bfs(S))
