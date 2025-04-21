# 중복 가능; 순서는 무관함
# m개 고르기
# 고른 수열은 오름차순이어야 함

N, M = map(int, input().split())
ptr = 1
def combination(arr, r):
    arr.sort()
    def generate(start, chosen):
        if len(chosen) == r:
            print(' '.join(map(str, chosen)))
            return
        for i in range(start, N+1):
            chosen.append(i)
            # print("gen {}, {}".format(i, chosen))
            generate(i, chosen)
            chosen.pop()
    generate(1, [])
combination([x for x in range(1, N+1)], M)