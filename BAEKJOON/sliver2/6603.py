# kC6 조합 문제
from itertools import combinations

while True:
    cmd = list(map(int,input().split()))
    if len(cmd) == 1:
        break
    k = cmd[0]
    slist = cmd[1:]
    # print(k, slist)
    for tmp in combinations(slist, 6):
        print(' '.join(map(str, tmp)))
    print()

