K = int(input())
stk = []

for _ in range(K):
    n = int(input())
    if n == 0:
        if len(stk): stk.pop(-1)
    else:
        stk.append(n)
print(sum(stk))