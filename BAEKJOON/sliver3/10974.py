from itertools import permutations
N = int(input())
li = [x for x in range(1, N+1)]
res = []
for p in permutations(li, N):
    res.append(p)
res.sort()
for i in res:
    print(" ".join(map(str, i)))
