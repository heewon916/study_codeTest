n = int(input())
dp = [0] * 301
p = [0] * 301
for i in range(n):
    p[i] = int(input())

dp[0] = p[0]
dp[1] = p[0] + p[1]
dp[2] = max(p[0]+p[2], p[1]+p[2])

# if n <= 2:
#     print(dp[n-1])
# else:
for i in range(3, n):
    dp[i] = max(dp[i-3]+p[i-1]+p[i], dp[i-2]+p[i])

print(dp[n-1])