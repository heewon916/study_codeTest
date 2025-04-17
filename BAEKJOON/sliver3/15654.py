N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))
l = []
def dfs(idx):
    if len(l) == M:
        print(' '.join(map(str,l)))
        return
    for i in range(idx+1, len(arr)):
        l.append(arr[i])
        dfs(i)
        l.pop()

dfs(-1)