N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
ans = 0
for val in arr:
    if K == 0:
        break
    if K < val:
        continue
    else:
        ans = ans + K // val
        K = K % val
print(ans)