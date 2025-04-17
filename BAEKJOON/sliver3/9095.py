dp = [0] * (11)
dp[1] = 1
dp[2] = 1
for i in range(3, 11):
    dp[i] = dp[i-1] + dp[i-2]
for i in range(int(input())):
    a = int(input())
    print(dp[a])