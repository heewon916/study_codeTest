# 0과 11 만으로 만들 수 있는 N자리 이진수 개수
import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [0] * (N+1)
dp[1] = 1
if N > 1:
    dp[2] = 2
    for i in range(3, N+1): # 10^6번 간당간당
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[-1]%15746)