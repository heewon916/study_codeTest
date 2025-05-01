# n ~ 50,000 = 5 * 10^4
# 메모리 512mb = 2^9 * 10^6 ~= 4 * 10^8 개 저장 가능
import sys
from math import *
input = sys.stdin.readline
n = int(input())
cnt = 0
while n>1:
    sq_n =  floor(sqrt(n))
    # print('sq_n', sq_n)
    n = n - sq_n**2
    # print('n', n)
    cnt += 1
print(cnt)