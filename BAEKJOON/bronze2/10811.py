n, m = map(int, input().split())

bkt = [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    tmp = bkt[a-1:b]
    bkt = bkt[:a-1] + tmp[::-1] + bkt[b:]
    # print(bkt)
for i in bkt: 
    print(i, end = ' ')
# 12345
# 21345
# 21435
# 34125
