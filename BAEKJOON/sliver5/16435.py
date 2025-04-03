# 하나 먹으면 길이 +1
# 과일 높이 hi (N개)
# 자신의 길이 >= hi 인 과일들을 먹을 수 있다.
# 처음 길이 L -> 과일들을 먹어 늘릴 수 있는 최대 길이 구하기

N, L = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for i in range(N):
    if h[i] <= L:
        L += 1
print(L)