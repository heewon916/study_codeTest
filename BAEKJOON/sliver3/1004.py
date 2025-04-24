T = int(input())
for _ in range(T):
    startX, startY, endX, endY = map(int, input().split())
    N = int(input())
    li = [tuple(map(int, input().split())) for _ in range(N)]
