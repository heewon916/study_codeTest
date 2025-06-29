import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
M = int(input().rstrip())

arr.sort()
left = 0
right = arr[-1]
while left <= right:
    mid = (left + right) // 2
    total = 0
    for n in arr:
        if n <= mid: total += n
        else: total += mid
    if total <= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)
