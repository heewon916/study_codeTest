N = int(input())
d = {}
arr = list(map(int, input().split()))
for i in range(N):
    d[i+1] = arr[i]
d_sorted = dict(sorted(d.items(), key=lambda x:x[1]))
total = 0
wait = 0
for t in d_sorted.values():
    wait = wait + t
    total += wait
print(total)