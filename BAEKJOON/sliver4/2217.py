# N개의 로프
# k개의 로프로 w 물체 들어올림 -> 각 로프 w/k만큼의 중량
# 들어올릴 수 있는 최대 중량

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
# 각 로프가 버틸 수 있는 최대 중량
R = [int(input().rstrip()) for _ in range(N)]
R.sort(reverse=True)
res = 0
# 로프들을 이용해 들어올릴 수 있는 물체의 최대 중량
for i in range(1, N+1):
    res = max(res, R[i-1]*i)
    # tmp = R[:i]
    # res = max(res, tmp[-1]*len(tmp))
    # print(res)
print(res)
