import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = [input().rstrip() for _ in range(N)]
b = [input().rstrip() for _ in range(M)]
res = list(set(a).intersection(set(b)))
res.sort()
print(len(res))
for n in res:
    print(n)