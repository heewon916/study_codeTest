K = int(input())
# 각 반의 수학 성적 - max, min, largest gap
for c in range(1, K+1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    li = tmp[1:]
    print("Class {}".format(c))
    li.sort(reverse=True)
    diff = 0
    for i in range(len(li)-1):
        # print(li[i] - li[i+1], diff)
        diff = max(li[i] - li[i+1], diff)
    print("Max {}, Min {}, Largest gap {}".format(max(li), min(li), diff))
