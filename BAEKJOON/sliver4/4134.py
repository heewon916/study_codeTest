import sys
import math
input = sys.stdin.readline

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    if n == 0 or n == 1:
        print(2)
    else:
        while 1:
            if prime(n):
                print(n)
                break
            else:
                n+=1