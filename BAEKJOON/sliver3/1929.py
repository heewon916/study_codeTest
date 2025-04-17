import sys, math
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

for i in range(a, b+1):
    if i == 1: continue
    else:
        if prime(i): print(i)