import heapq as hq
N = int(input())

h = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if not h: print(0)
        else: print(hq.heappop(h)[1])
    else:
        hq.heappush(h, (abs(n), n))


