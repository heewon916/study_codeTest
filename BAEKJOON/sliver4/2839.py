N = int(input())
cnt = 0

while N>0:
    if N%5 == 0:
        cnt += N//5
        N = N % 5
        break
    N -= 3
    cnt += 1
if N:
    print(-1)
else:
    print(cnt)


# while True:
#     N -= 5
#     if N < 0:
#         N += 5
#         break
#     cnt += 1
#     print(N, cnt)
# if N%3 == 0:
#     cnt += (N//3)
#     print(cnt)
# else:
#     print(-1)