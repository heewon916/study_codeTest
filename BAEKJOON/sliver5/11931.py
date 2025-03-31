
import heapq as hq
import sys 
input = sys.stdin.readline

N = int(input())
li = []
for i in range(N):
    hq.heappush(li, -int(input()))
    
hq.heapify(list(set(li)))
for _ in range(N):
    print(-hq.heappop(li))

## 시간초과 풀이 - hq 사용



