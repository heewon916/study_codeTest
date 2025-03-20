import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x:
        hq.heappush(h, -x)
    else:
        if h:
            print(-hq.heappop(h))
        else:
            print(0)