import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set([input().rstrip() for _ in range(N)])
M_s = [input().rstrip() for _ in range(M)]
cnt = 0
for ms in M_s:
    if ms in S:
       cnt += 1

print(cnt)
# print(S, M_s)
# print(len(M_s.intersection(S)))