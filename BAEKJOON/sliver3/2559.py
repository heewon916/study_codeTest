#N: 10^5; K:10^5; 이중반복문 불가
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
dp = [0] * (N-K+1)
dp[0] = sum(li[0:K])
for i in range(1, N-K+1):
    dp[i] = li[i+K-1] + dp[i-1] -li[i-1]
print(max(dp))
### 시간초과
# max_v = 0
# for i in range(N-K+1):
#     max_v = max(max_v, sum(li[i:i+K]))
# print(max_v)
