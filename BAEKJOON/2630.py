n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
w = 0; b = 0
def div_conq(x, y, n):
    # 각 범위 안에서 체크
    global w, b, graph
    cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] == 1: # blue 이면 1 증가
                cnt += 1
    if cnt == 0 : # 0 이면 전부 흰색 의미
        w += 1
    elif cnt == n**2: # 1이면 전부 파랑 의미
        b += 1
    else: # 4분할 필요
        div_conq(x, y, n//2)
        div_conq(x+n//2, y, n//2)
        div_conq(x, y+n//2, n//2)
        div_conq(x+n//2, y + n // 2, n // 2)

div_conq(0, 0, n)
print(w)
print(b)

# def multi(pt1, pt2):
#     i1, j1 = pt1
#     i2, j2 = pt2
#     total = graph[i1][j1]
#     for i in range(i1, i2 + 1):
#         for j in range(j1, j2 + 1):
#             total *= graph[i][j]
#             if total != graph[i1][j1]:  # 값이 변하면
#                 return 0 # 쪼개야 됨
#     return 1 # 하나의 정사각형 완료!
# def check(pt1, pt2, N):
#     global w, b, graph
#     i1, j1 = pt1
#     # i2, j2 = pt2
#     if N == 1:
#         if graph[i1][j1] == 1: # blue
#             b += 1
#         else: # white
#             w += 1
#         return
#     else:
#         if multi(pt1, pt2):
#             if graph[i1][j1] == 1: b += 1
#             else: w += 1
#         else:
#             check((i1, ))
# check((0,0), (n-1,n-1), n)