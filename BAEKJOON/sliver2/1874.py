import sys
input = sys.stdin.readline

n = int(input())
target = [int(input()) for _ in range(n)]

stack = []
idx = 0
res = ''
for i in range(1, n+1):
    stack.append(i)
    res += '+'
    while stack and idx < n and stack[-1] == target[idx]:
        stack.pop(-1)
        res += '-'
        idx += 1
if stack:
    print('NO')
else:
    print('\n'.join(res))