import sys
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())
count = 0
while B>A:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break
    count += 1
if B == A:
    print(count+1)
else:
    print(-1)