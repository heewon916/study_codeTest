import sys
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep2814_input.txt", "r")

T = int(input())

def dfs(node, cnt):
    global visited, ans
    visited[node] = 1
    for v in graph[node]:
        if not visited[v]:
            visited[v] = 1
            dfs(v, cnt + 1)
    visited[node] = 0
    ans = max(ans, cnt)

for tc in range(1, T+1):
    # n개의 정점과 m개의 간선
    n,m = map(int, input().split())
    # 전체 저장 x 간선 == 1만 저장
    # 정점 번호 1~n
    graph = [[0] for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    ans = 1
    for i in range(1, n+1):
        visited = [0] * (n+1)  # 정점의 개수만큼 visited 개수 세기
        dfs(i, 0)
        # if not visited[i]:
        #     visited[i] = 1
        #     dfs(i, 1)
        #     visited[i] = 0

    print("#{} {}".format(tc, ans))