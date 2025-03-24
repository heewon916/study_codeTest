#0 1 1 2 3 5 8 13 21 
# 6 
# 5 4
# 4 3 3 2 
# 3 2 2 1 2 1 
# 2 1 
## -> 재귀함수에서 1과 2를 만났을 때 return 1; 하는 횟수는 dp[n]과 같다. 
dp = [0]*41
dp[0] = 0 
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

f = [0] * 41
count = 0
def fib_dp(n):
    global f, count
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count += 1
    return f[n]

n = int(input())
fib_dp(n)
print(dp[n], count)

## 다른 풀이 
import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a+b 
print(a, n-2)