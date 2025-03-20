import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if arr:
            print(hq.heappop(arr))
        else:
            print(0)
    else:
        hq.heappush(arr, x)
