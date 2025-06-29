N, K = map(int, input().split())

res, div = 1, 1
for i in range(K):
    res *= N
    N -= 1

for i in range(2, K+1):
     div *= i

print((res//div) % 10007)

