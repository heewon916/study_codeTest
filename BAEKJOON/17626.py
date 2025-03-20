import sys
from math import *
input = sys.stdin.readline
n = int(input())
cnt = 0
while n>1:
    sq_n =  floor(sqrt(n))
    print('sq_n', sq_n)
    n = n - sq_n**2
    print('n', n)
    cnt += 1
print(cnt)