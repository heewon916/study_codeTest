import sys

N = int(input())
sys.setrecursionlimit(10**6)
INF = 987654321
cache = [INF] * (N+1)
cache[1] = 0

def dp(n):
    if cache[n] != INF:
        return cache[n]
    if n%6 == 0:
        cache[n] = min(dp(n//3), dp(n//2)) + 1
    elif n%3 == 0:
        cache[n] = min(dp(n//3), dp(n-1))  + 1
    elif n%2 == 0:
        cache[n] = min(dp(n//2), dp(n-1)) + 1
    else:
        cache[n] = dp(n-1) + 1
    return cache[n]

print(dp(N))

