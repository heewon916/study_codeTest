# 111
# => 011 + 001 + 010 - 000
# 011 => 1
# 001 => 1
# 010 => 1
# 000 => 1
#
# 222
# => 122 + 112 + 121 - 111
#
# 결국 dp 문제이다. 앞서 계산한 상황을 다시 계산하지 않도록 저장해야 한다.
# 이때 a,b,c를 딕셔너리로 묶어서 저장하면 편할 것 같다.
# dp = {(0,0,0): 1}
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
for a in range(21):
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0:
                dp[a][b][c] = 1
            elif a < b < c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

while True:
    a, b, c = map(int, input().split())
    if (a,b,c) == (-1,-1,-1): break
    else:
        if a <= 0 or b <= 0 or c <= 0:
            print('w({}, {}, {}) = {}'.format(a,b,c, 1))
        elif a > 20 or b > 20 or c > 20:
            print('w({}, {}, {}) = {}'.format(a, b, c, dp[20][20][20]))
        else:
            print('w({}, {}, {}) = {}'.format(a, b, c, dp[a][b][c]))
