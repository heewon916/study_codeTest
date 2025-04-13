import sys
input = sys.stdin.readline

N = input().rstrip()
res = 0
for i in range(len(N)-1):
    res += 9*(10**i) * (i+1)
res += (int(N) - (10**(len(N)-1)) + 1) * len(N)

print(res)
