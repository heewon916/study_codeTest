import sys
input = sys.stdin.readline
### DP
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)  # N일까지 포함해서 dp 배열 만들기

for i in range(N - 1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])

print(dp[0])

N = int(input().rstrip())
tp = [tuple((map(int,input().rstrip().split()))) for _ in range(N)]

# k일차 상담은 무조건 한다고 했을 때. (k=1..N)
### 백트래킹
# max_profit = 0
# def backtrack(day, current_profit):
#     global max_profit
#     if day >= N:
#         max_profit = max(current_profit, max_profit)
#         return
#     T, P = tp[day]
#     # 상담 할 경우
#     if day+T <= N:
#         backtrack(day+T, current_profit+P)
#
#     backtrack(day+1, current_profit)
# backtrack(0, 0)
# print(max_profit)
### 재귀함수 only
# def benefit(day):
#     if day >= N: # day가 퇴사일보다 크거나 같으면 상담 불가능
#         return 0
#     T, P = tp[day]
#
#     # day+T 했을 때 상담을 퇴사일 당일까지 완료할 수 있다면
#     if day+T <= N:
#         take = P + benefit(day+T)
#         skip = benefit(day+1)
#         return max(take, skip)
#     else:
#         return benefit(day+1)
# print(benefit(0))
