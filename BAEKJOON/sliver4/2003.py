import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
# 투포인터
i = 0
j= 1
cnt = 0
while i <= j <= N:
    s = sum(A[i:j])
    if s == M:
        cnt += 1
        j += 1
    elif s < M:
        j += 1
    elif s > M:
        i += 1
print(cnt)
# S = [0] * (N + 1)
# for i in range(1, N + 1):
#     S[i] = A[i - 1] + S[i - 1]
# cnt = 0
# for i in range(N+1):
#     for j in range(i, N+1):
#         if S[j] - S[i-1] == M: cnt += 1
# print(cnt)