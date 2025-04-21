import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
dp = [0] * (N+1)
dp[1] = li[0]
for i in range(1, N+1):
    dp[i] = li[i-1] + dp[i-1]

# 1초니까 10^8까지 가능
for _ in range(M):
    i, j = map(int, input().rstrip().split())
    print(dp[j] - dp[i-1])
    # print(sum(li[i-1:j]))