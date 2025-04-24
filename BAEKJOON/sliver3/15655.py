# 중복 불가; 조합으로 따짐
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
li.sort()

for i in combinations(li, M):
    print(' '.join(map(str, i)))