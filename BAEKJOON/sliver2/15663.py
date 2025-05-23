from itertools import permutations
N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

res = set()
for p in permutations(li, M):
    res.add(p)
res = list(res)
res.sort()
for c in res:
    print(' '.join(map(str, c)))