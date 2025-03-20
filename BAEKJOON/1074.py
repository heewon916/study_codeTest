import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**3)
N, r, c = map(int, input().split())


def dc(n, r, c, res):
    length = 2**n
    half = length // 2
    if n == 1: # 재귀 종료조건 2x2 4 최소 사분면이 만들어질 경우
        print(2 * r + c + res)  # row가 늘어나면 도착횟수가 2씩 늘어나고 colunm이 늘어나면 1씩 늘어난다.
        return

    if r < half and c < half: # 1사분면
        dc(n-1, r, c, res)
    elif r < half and c >= half: # 2사분면
        dc(n-1, r, c-half, res+half*half)
    elif r >= half and c < half: # 3사분면
        dc(n-1, r-half, c, res+2*half*half)
    else: # 4사분면
        dc(n - 1, r - half, c-half, res + 3 * half * half)


dc(N, r, c, 0)


################## 시간 초과 코드 ##########
# cnt = -1
#
# def z(x, y, n):
#     global r, c, cnt
#     if n == 1:
#         cnt += 1
#         if x == r and y ==c:
#             print(x,y, cnt)
#             exit()
#     else:
#         z(x, y, n//2)
#         z(x, y+n//2, n//2)
#         z(x+n//2, y, n//2)
#         z(x+n//2,y+n//2, n//2)
#
# z(0, 0, 2**N)
