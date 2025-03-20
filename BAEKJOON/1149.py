n = int(input())    # n개의 집
rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(n)]
dp[0] = rgb[0]

for i in range(1, n):
    # min값은 rgb에서 고르는 게 아니라, dp(누적된 값)에서 비교해서 골라야지..
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + rgb[i][2]
    #print(dp)


print(min(dp[n-1]))