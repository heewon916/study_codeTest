# 한번에 1개, 2개
# 연속된 3개 불가.
# 시작점은 계단에 포함 노노
# 마지막은 꼭 밟아야함

# 마지막 계단에서부터 거꾸로 계산해본다고 상상하면,
# 전 계단을 포함하냐 안하냐 비교
# 연속 3개면 out.

import sys
input = sys.stdin.readline

N = int(input().rstrip())
score = [int(input().rstrip()) for _ in range(N)]
comboCount = 0
dp = [0] * (N+1)
dp[0] = score[0]
dp[1] =
# max_score = stairs[-1]
# for i in range(N-1, -1, -1):
