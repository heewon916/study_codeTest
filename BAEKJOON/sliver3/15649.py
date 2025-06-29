N, M = map(int, input().split())
array = []

def backtracking():
    if len(array) == M:
        print(' '.join(map(str, array)))
        return
    for i in range(1, N+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()
backtracking()

### dfs로 푼 경우 ###
visited = [0] * (N+1)
def dfs():
    if len(array) == M:
        print(' '.join(map(str, array)))
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        array.append(i)
        dfs()
        array.pop()
        visited[i] = 0
dfs()
### 라이브러리로 푼 경우 ###
# from itertools import permutations
# N, M = map(int, input().split())
# li = [x for x in range(1, N+1)]
# res = []
# for tmp in permutations(li, M):
#     res.append(list(tmp))
# res.sort()
# for i in res:
#     print(' '.join(map(str,i)))