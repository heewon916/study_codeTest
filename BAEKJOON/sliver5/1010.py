# from itertools import combinations
for ts in range(int(input())):
    n,m = map(int, input().split())
    # 하나 고르면 그 다리 이후의 다리와만 연결이 가능하다. 
    # 단 동쪽 다리에는 최소한 서쪽에 연결 안된 사이트 개수만큼은 남아있어야 한다. 
    # print(len(list(combinations(range(m), n))))
    up = 1
    for i in range(n):
        up *= m
        m -= 1
    down = 1 
    for i in range(n):
        down *= n 
        n -= 1
    print(up // down)