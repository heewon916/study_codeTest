def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
N = int(input())
li = list(map(int, input().split()))
for i in range(1, N):
    g = gcd(li[0], li[i])
    print("{}/{}".format(li[0]//g, li[i]//g))