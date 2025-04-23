
import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = list(map(int, input().rstrip().split()))
li.sort()
x = int(input().rstrip())


left = 0
right = N-1
count = 0
while left < right:
    total = li[left] + li[right]
    if total == x:
        count += 1
        left += 1
        right -= 1
    elif total < x:
        left += 1
    elif total > x:
        right -= 1
print(count)