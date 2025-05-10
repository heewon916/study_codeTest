import heapq
import sys
input = sys.stdin.readline
hp = []
N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if len(hp):
            print(heapq.heappop(hp))
        else: print(0)
    else:
        heapq.heappush(hp, x)