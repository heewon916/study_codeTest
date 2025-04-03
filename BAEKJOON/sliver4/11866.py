from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
ans = []
while q:
    for i in range(k-1):
        v = q.popleft()
        q.append(v)
    ans.append(q.popleft())
print("<", end='')
for i in range(n):
    if i < n-1:
        print(ans[i], end=', ')
    if i == n-1:
        print(ans[i], end='')
print(">")

