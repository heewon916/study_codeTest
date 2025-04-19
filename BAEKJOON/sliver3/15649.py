from itertools import permutations
N, M = map(int, input().split())
li = [x for x in range(1, N+1)]
res = []
for tmp in permutations(li, M):
    res.append(list(tmp))
res.sort()
for i in res:
    print(' '.join(map(str,i)))