import sys 
from itertools import permutations
input = sys.stdin.readline 

N = list(map(int, input().rstrip()))
if 0 not in N or sum(N)%3 != 0:
    print(-1)
else:
    print(''.join(map(str, sorted(N, reverse=True))))

