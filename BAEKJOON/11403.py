N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# output = [[0 for _ in range(N)] for _ in range(N)]
output = [0 for _ in range(N)]
def dfs(n):
    for i in range(N):
        if graph[n][i] == 1 and output[i] == 0:
            # output[n][i] = 1 이렇게 하면 도돌이표, 각 점에 대한 output이 필요
            output[i] = 1
            dfs(i)


for i in range(N):
    dfs(i)
    for j in range(N):
        print(output[j], end = ' ')
    print()
    output = [0 for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         print(output[i][j], end= ' ')
#     print()


