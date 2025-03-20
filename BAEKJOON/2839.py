N = int(input())

if N % 5 == 0:
    ans = N // 5
elif (N%5)%3 == 0 or (N%3)%5 == 0:
    ans = 