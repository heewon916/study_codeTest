from itertools import combinations
n, m = map(int, input().split())
n_s = list(map(int, input().split()))
mx = 0
l = list(combinations(n_s, 3))
# l = list().sort(key=lambda x:sum(x), reverse=True)
for i in l:
    if m >= sum(i) > mx:
        mx = sum(i)
print(mx)