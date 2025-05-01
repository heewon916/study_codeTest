N = int(input())
# 큰 수 N개만 저장하는 리스트
nlist = []

for i in range(N):
    if i == 0: nlist = list(map(int, input().split()))
    else:
        tmp = list(map(int, input().split()))
        for c in tmp:
            nlist.append(c)
    nlist.sort(reverse=True)
    nlist = nlist[:N]
    # print(nlist)
print(nlist[-1])