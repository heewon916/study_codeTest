# N: 스크린의 크기, M: 바구니의 크기  N>M
N, M = map(int, input().split())
J = int(input())
bkt = [1, M]
dist = 0
for _ in range(J):
    pos = int(input())
    while True:
        if bkt[0] <= pos <= bkt[1]:
            break
        elif pos < bkt[0]:
            dist += bkt[0]-pos
            bkt[0] -= bkt[0] - pos
            bkt[1] -= bkt[0] - pos
        elif pos > bkt[1]:
            dist += pos - bkt[1]
            bkt[0] += pos - bkt[1]
            bkt[1] += pos - bkt[1]
print(dist)