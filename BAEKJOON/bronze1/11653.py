n = int(input())
factors = []

# 2로 나누기 
while n%2 == 0: 
    n //= 2 
    factors.append(2)
    
# 3, 5, 7 홀수로 나누기 
# - 제곱수 이용해서 루트 n까지만 연산하기 
i = 3
while i*i <= n: 
    while n%i == 0: 
        n //= i 
        factors.append(i)
    i += 2 
# 마지막으로 남는 숫자 n이 1이 아니면 소수니까 포함시키기기

if n > 1: 
    factors.append(n)
for i in factors:
    print(i)