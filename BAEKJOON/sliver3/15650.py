from itertools import combinations
N,M = map(int, input().split())
li = [x for x in range(1, N+1)]
res = []
for l in combinations(li, M):
    res.append(list(l))
for l in res:
    print(' '.join(map(str, l)))