diff = []
cnt = 0
for i in range(10):
    n = int(input())
    if n%42 not in diff:
        diff.append(n%42)
        cnt += 1
print(cnt)