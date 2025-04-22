N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

visited = [0] * N # 중복 불가

def generate(chosen):
    if len(chosen) == M:
        print(' '.join(map(str, chosen)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            chosen.append(li[i])
            generate(chosen)
            chosen.pop()
            visited[i] = 0

generate([])
