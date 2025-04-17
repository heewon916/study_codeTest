tc = int(input())
dp = [0]  * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(6, 9):
    dp[i] = dp[9-i] + dp[i-1]
for i in range(9, 101):
    dp[i] = dp[i-5] + dp[i-1]
for _ in range(tc):
    n = int(input())
    print(dp[n])
