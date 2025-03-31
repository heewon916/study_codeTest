import sys 
input = sys.stdin.readline
N = int(input())

graph = [input().rstrip() for _ in range(N)]
r, c = 0, 0

for row in graph: 
    if '..' in row: 
        r += 1

for row in list(zip(*graph)):
    if '..' in ''.join(row): 
        c += 1
print(r, c)
# import sys 
# input = sys.stdin.readline
# N = int(input())

# graph = [list(map(str, input().rstrip())) for _ in range(N)]
# r, c = 0, 0
# for i in range(N):
#     len_r, len_c = 0, 0
#     for j in range(N): 
#         if graph[i][j] == '.':
#             len_r += 1
#         else: 
#             len_r = 0 
#         if len_r == 2: 
#             r += 1
        
#         if graph[j][i] == '.':
#             len_c += 1
#         else: 
#             len_c = 0
#         if len_c == 2: 
#             c += 1
# print(r, c)

    