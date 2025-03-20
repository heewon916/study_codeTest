n = int(input())
a = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
# dp = [0 for _ in range(n)]
# dp[-1] = 1
# top = 1001
#
# for i in range(n-2, -1, -1):
#     print(top, a[i], a[i+1])
#     if a[i] < a[i+1] and a[i] < top:
#         dp[i] = dp[i+1] + 1
#         top = a[i]
#     else:
#         dp[i] = dp[i+1]
#
# print(dp[0])