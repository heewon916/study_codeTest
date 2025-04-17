import sys
input = sys.stdin.readline
N = int(input().strip())
dp = [0] * (N+1)
dp[2] = 1
dp[3] = 1
for i in range(4, N+1):
    if i%3 == 0:
        dp[i] = dp[i//3] + 1
    else:
        if i%2 != 0:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = min(dp[i-1]+1, dp[i//2]+1)
print(dp[N])
