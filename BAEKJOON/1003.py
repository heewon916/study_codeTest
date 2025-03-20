T = int(input())
# dp = [-1] * 41 ==> 굳이 필요없는 코드
# dp[0] = 0
# dp[1] = 1

zero_cnt = [0] * 41
one_cnt = [0] * 41

zero_cnt[0] = 1
one_cnt[1] = 1


for tc in range(T):
    n = int(input())
    if n > 1:
        for i in range(2, n+1):
            # dp[i] = dp[i-2] + dp[i-1]
            zero_cnt[i] = zero_cnt[i-1] + zero_cnt[i-2]
            one_cnt[i] = one_cnt[i-1] + one_cnt[i-2]
            # 아래서부터 전부 계산해 올라가기
    print(zero_cnt[n], one_cnt[n])