# 이중 반복문 불가능
import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = list(map(int, input().rstrip().split()))

dp = [0] * N
dp[0] = li[0]
# 1부터 시작하는 이유: 0번 인덱스는 이전까지의 합이 0 자신 자체이므로 아무런 필요가 없다.
for i in range(1, N):
    # 누적해서 더할지, 그냥 이 시점부터 다시 시작할지를 택한다.
    # 즉, 직전까지의 합이 양수인 경우에는 i번째 원소를 더한 값이최댓값이 되고, 음수인 경우에는 i번째 원소만 있는 경우가 최댓값이 될 것이다.
    dp[i] = max(dp[i-1]+li[i], li[i])

# print(dp)
print(max(dp))