import heapq
l = [64]
x = int(input())
while True: 
    if sum(l) == x: 
        print(len(l))
        break  
    half = heapq.heappop(l) // 2
    if sum(l) + half >= x: 
        heapq.heappush(l, half)
    else:
        heapq.heappush(l, half)
        heapq.heappush(l, half)
    # print(l)
    