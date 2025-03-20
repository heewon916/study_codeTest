import heapq as hq
n = int(input())
h = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    for c in tmp:
        if len(h) < n:
            hq.heappush(h, c)
        else: # 작은 숫자는 차례 차례 없애고 큰 숫자들로 채우는 거지 !!
            hq.heappush(h, c)
            hq.heappop(h)

print(h[0])