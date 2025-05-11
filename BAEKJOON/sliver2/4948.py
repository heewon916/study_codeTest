import math
def chkPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
dp = [0] * (123457*2)
for i in range(2, 123457*2):
    if chkPrime(i): dp[i] = 1

while True:
    n = int(input())
    if n == 0: break
    print(dp[n+1:2*n+1].count(1))
# while True:
#     cnt = 0
#     n = int(input())
#     if n == 0: break
#     for i in range(n+1, 2*n+1):
#         if chkPrime(i): cnt += 1
#     print(cnt)