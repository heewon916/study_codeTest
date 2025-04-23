# 일직선 도로 위 n개의 도시
# 출발 할 때 기름 0 -> 넣고 출발
# 1키로마다 1리터 기름 사용

# 가격 * 리터 누적합의 최소
# N: 2-10^5; 거리: 1-10^9; 가격: 1-10^9
# 제한시간 2초; 2 * 10^8
# 512MB = 2^9 * 1024 * 1024 = 2^9 * 10^6 ~= 10^9

import sys
input = sys.stdin.readline

N = int(input().rstrip()) #N개의 도시
roads = list(map(int, input().rstrip().split())) # N-1개의 도로
prices = list(map(int, input().rstrip().split())) # N개의 주유소 가격

total_price = 0
min_price = prices[0]
for i in range(N-1):
    if prices[i] < min_price:
        min_price = prices[i]
    total_price += min_price * roads[i]
print(total_price)