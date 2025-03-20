import sys
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep9229_input.txt", "r")
from itertools import combinations
T = int(input())

for tc in range(1, T+1):
    n, limit = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    for tmp in combinations(arr, 2):
        if sum(tmp) <= limit:
            result = max(result, sum(tmp))
    if result == 0:
        print(-1)
    else:
        print(result)