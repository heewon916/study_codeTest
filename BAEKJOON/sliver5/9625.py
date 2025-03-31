# A, B, BA, BAB, BABBA, BABBABAB .
# 모든 B -> BA/ A -> B 
K = int(input())
dp = [0] * (K+2)
dp[0] = 0 
dp[1] = 1
for i in range(2,K+2):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[K-1], dp[K])

## IndexError: A와 B의 인덱스 차이 고려 안함 
# dp_a = [0] * (K+1)
# dp_b = [0] * (K+1)
# dp_a[0] = 1; dp_a[1] = 0; dp_a[2] = 1
# dp_b[0] = 0; dp_b[1] = 1 

# for i in range(2,K+1):
#     dp_a[i] = dp_a[i-1] + dp_a[i-2]
#     dp_b[i] = dp_b[i-1] + dp_b[i-2]
# print(dp_a[K], dp_b[K])

## 시간초과 풀이 
# K = int(input())
# s = 'A'
# for _ in range(K):
#     tmp = ''
#     for i in s: 
#         if i == 'A': tmp += 'B'
#         elif i == "B": tmp += 'BA'
#     s = tmp 
# print(s.count('A'), s.count('B'))