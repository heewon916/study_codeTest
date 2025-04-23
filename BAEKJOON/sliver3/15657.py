# 수열 내 숫자 중복 가능
# 같은 조합 중복 불가 (1,7) 있으면 (7,1) 불가

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

def generate(start, chosen):
    if len(chosen) == M:
        print(' '.join(map(str, chosen)))
        return
    for i in range(start, N):
        chosen.append(li[i])
        generate(i, chosen)
        chosen.pop()

generate(0, [])