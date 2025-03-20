import sys
input = sys.stdin.readline
L = int(input())
total = 0
M = 1234567891
r = 31
for i, c in enumerate(input()):
    if c.isalpha():
        n = (ord(c)-ord('a')+1)*(r**i)
        total += n
print(total % M)