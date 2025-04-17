# M개 고르기
# 중복 고르기 가능
# 오름차순

N,M = map(int,input().split())
arr = []
def dfs(n):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(n, N+1):
        arr.append(i)
        dfs(i)
        arr.pop()       # 백트래킹

dfs(1)