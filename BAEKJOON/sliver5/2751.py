import sys, heapq
input = sys.stdin.readline 

li = []
for i in range(int(input())):
    n = int(input())
    heapq.heappush(li, n)
    
for i in range(len(li)):
    print(heapq.heappop(li))
    
