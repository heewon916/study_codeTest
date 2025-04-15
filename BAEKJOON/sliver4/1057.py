import sys
input = sys.stdin.readline

N, a, b = map(int, input().strip().split())

round = 0
while a != b:
    a = (a+1)//2
    b = (b+1)//2
    round += 1

print(round)