from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nlist = list(map(int, input().split()))
# N개의 재료는 각각 고유의 번호를 갖는다. 이 번호들을 합쳐서 M을 만들 수 있는 경우의 수를 구해야 한다.

# 단 범위가 M = 10^7, N = 15000
nlist.sort()
left = 0
right = N-1
cnt = 0
while left < right:
    total = nlist[left] + nlist[right]
    if total == M:
        cnt += 1
        left += 1
        right -= 1
    elif total < M:
        left += 1
    elif total > M:
        right -= 1
print(cnt)

