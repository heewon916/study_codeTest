import sys
input = sys.stdin.readline
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
for _ in range(int(input().rstrip())):
    n, *li = map(int, input().rstrip().split())
    res = 0
    for i in range(n-1):
        for j in range(i+1, n):
           res += gcd(li[i], li[j])
    print(res)