import sys
K = int(sys.stdin.readline())
stck = []
for i in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        if stck: stck.pop()
        else: continue
    else:
        stck.append(n)
print(sum(stck))
