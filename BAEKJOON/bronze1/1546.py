n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
total = 0
for i in range(n):
    tmp = arr[i] / m * 100
    total += tmp
print(total/n)
