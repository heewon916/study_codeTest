N = int(input()) #전체 사람 명수: 번호 1~100 
a, b = map(int, input().split())
M = int(input()) #부모자식 관계 개수 
graph = [[] for _ in range(N+1)] #부모자식 관계 연결리스트 
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(N+1)] # 방문한 사람은 또 방문하지 X 
result = 0 
def dfs(start,cnt):
    global result
    visited[start] = True 
    if start == b: # 간선의 개수 구하기
         result = cnt
    else:
        for con in graph[start]:
            if visited[con] == False:
                #print(f"NEXT dfs({con, cnt+1})")
                dfs(con, cnt+1)
    
dfs(a, 0)
if result == 0: 
    print(-1)
else:
    print(result)

# N = int(input()) #전체 사람 명수 
# a, b = map(int, input().split()) # 촌수를 계산해야 하는 사람 번호 (1~100)
# print(f"a={a} b={b}")
# M = int(input()) # 부모 자식들 간 관계의 개수 
# # 단방향 그래프 같긴 한데, 그렇게 구현하면 탐색하기 힘들 것 같으니 그냥 양방향
# # 이렇게 그래프 만들 수도 있구나~! 
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#   x, y = map(int, input().split())  
#   graph[x].append(y)
#   graph[y].append(x)
# #graph = [[0]*(N+1) for _ in range(N+1)]
# # for _ in range(relation):
# #     parent, child = map(int, input().split())
# #     graph[parent][child] = 1
# #     graph[child][parent] = 1  
    
# # 한 쪽으로 깊게 파고 들어가니까 dfs일 것 같은데
# visited = [False for _ in range(N+1)]  # 사람 명수! 
# # visited = [[0]*(N+1) for _ in range(N+1)]
# result = 0
# q = []

# def dfs(start, cnt):
#     global result
#     visited[start] = True 
#     print(f"START start={start} cnt={cnt}")
#     if start == b:
#         result = cnt 
#         print("start == b", start)
#     for adj in graph[start]:
#         if not visited[adj]:
#             print(f"\tadj = {adj} => DFS({adj})")
#             dfs(adj, cnt+1)
#     # for i in range(N):
#     #     if  and not visited[start][i]: 
#     #         count += graph[start][i]
#     #         visited[start][i] = visited[i][start] = 1
#     #         if i == b:
#     #             count += graph[start][i]
#     #             return 
#     #         dfs(i)
# dfs(a, 0)
# print(result)

# # 아 근데 최단경로..?
            
            
    
    

