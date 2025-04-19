one_cnt = [0] * 41
one_cnt[1] = 1
one_cnt[2] = 1
for i in range(3, 41):
    one_cnt[i] = one_cnt[i-1] + one_cnt[i-2]

# 0횟수: dp[i]이면, 1횟수는 dp[i+1]
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(1, 0)
    else:
        print(one_cnt[n-1], one_cnt[n])