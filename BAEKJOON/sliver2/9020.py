# 2보다 큰 모든 짝수 = 두 소수의 합
import math
def chkPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True
for _ in range(int(input())):
    n = int(input())
    # n//2부터 소수를 찾고, 뺀 숫자 값도 소수이면 체크
    for p in range(n//2, n):
        if chkPrime(p) and chkPrime(n-p):
            print(n-p, p)
            break