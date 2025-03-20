a, b, c = map(int, input().split())

cnt = 0
while cnt <= b:
    a = a*a
    cnt += 1
    if a <= c:
        continue
    elif a > c:
        a = a % c
print(a)