# 가장 긴 증가하는 부분 수열을 구하라
# 시작점 start에 대해서, 증가하는 데까지 카운트한다. 이를 모든 원소에 대해 시행해야 하므로, N~1000 -> 1초 가능

N = int(input())
li = list(map(int, input().split(' ')))
dp = [0] * N
# li[i]를 마지막 원소 갖는 가장 긴 증가부분수열의 길이를 dp[i]라고 한다면?
for i in range(N):
    for j in range(i):
        if li[j] < li[i]:
            # 기존에 있는 수열하고, j위치부터 세는 수열 비교할 때 더 긴 수열을 택한다.
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp)+1)