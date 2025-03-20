exp = list(input().split('-'))
arr = []
for e in exp:
    total = 0
    tmp = list(map(int, e.split('+')))
    for j in tmp:
        total += j
    arr.append(total)
ans = arr[0]
for i in range(1, len(arr)):
    ans -= arr[i]
print(ans)