N = int(input())  # 수열의 길이
arr = list(map(int, input().split()))  # 수열 입력

dp = arr[:]  # dp 배열을 arr 배열의 복사로 초기화

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

# dp 배열에서 가장 큰 값이 가장 큰 증가 부분 수열의 합
print(max(dp))
