N, M = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(N):
    arr1.append(input())
for _ in range(M):
    arr2.append(input())
arr1 = set(arr1); arr2 = set(arr2)
ans = list(arr1.intersection(arr2))
ans.sort()
print(len(ans))
for a in ans:
    print(a)





