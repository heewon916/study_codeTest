# 중복 가능; 모든 수에 대해 처음부터
N, M = map(int, input().split())

def func(n, r):
    def generate(chosen):
        if len(chosen) == r:
            print(' '.join(map(str, chosen)))
            return
        for i in range(1,n+1):
            chosen.append(i)
            generate(chosen)
            chosen.pop()
    generate([])
func(N, M)