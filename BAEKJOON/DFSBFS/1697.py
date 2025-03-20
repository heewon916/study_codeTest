N, K = map(int, input().split())

# 가장 빠른 시간을 출력해야 하니 bfs가 맞다
q = [] 
visited = [0 for _ in range(100000+1)]
answer = 0
def bfs(n):
    global answer
    q.append(n)
    while q:
        v = q.pop(0)
        if v == K: 
            answer = visited[v]
            break
            # stop 
        nextpos = [v-1, v+1, 2*v]
        for i in range(3):
            if 0<=nextpos[i]<=100000 and not visited[nextpos[i]]:
                q.append(nextpos[i])
                visited[nextpos[i]] = visited[v] + 1
bfs(N)
print(answer)

###############################################################
# 시간 초과 코드 
# def bfs(n, time):
#     global answer
#     q.append((n, time))
#     while q:
#         v, t = q.pop(0)
#         visited.append(v)
#         #print(f"v={v} t={t}")
#         if v == K: 
#             answer = t
#             break
#             # stop 
#         nextpos = [v-1, v+1, 2*v]
#         for i in range(3):
#             if 0<=nextpos[i]<=100000 and nextpos[i] not in visited:
#                 #print(f"APPEND v={nextpos[i]}, t={t+1}")
#                 q.append((nextpos[i], t+1))
# bfs(N)
# print(answer)