# 1 1 1 2 2 3 4 5 7 8
# 0 1 2 3 4 5 6 7 8 9
# 3 = 0 + 1; 4 = 1 + 2
dp = [0] * 101
dp[0] = dp[1] = dp[2] = 1

for i in range(3, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(int(input())):
    N = int(input())
    print(dp[N-1])