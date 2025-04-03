# 피보나치 수열의 성질
N = int(input())
fib = [0] * 81
fib[0] = 0
fib[1] = 1
fib[2] = 1
for i in range(3, 81):
    fib[i] = fib[i-1] + fib[i-2]

# print(fib)
if N>=2:
    res = (fib[N]+fib[N-1])*2 + (fib[N-1]+fib[N-2])*2
else:
    res = 4
print(res)
