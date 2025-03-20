n, m = map(int, input().split())
bkt = [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    bkt[a-1], bkt[b-1] = bkt[b-1], bkt[a-1]
    # print(bkt)
for i in bkt:
    print(i, end=' ')