import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c, d = map(int, input().rstrip().split())

x, y = (a*d + b*c), b * d

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print(x//gcd(x,y), y//gcd(x,y))