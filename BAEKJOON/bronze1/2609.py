import sys
input = sys.stdin.readline
n, m = map(int, input().split())

a = min(n, m)
b = max(n, m)
# 최대 공약수
for i in range(a, -1, -1):
    if b%i == 0 and a%i == 0:
        print(i)
        break
# 최소 공배수
i = 1
while True:
    if (a*i) %b == 0:
        print(a*i)
        break
    else:
        i+=1