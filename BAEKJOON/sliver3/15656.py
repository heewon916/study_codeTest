# 중복 가능; 순열

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
li.sort()
def generate(chosen):
    if len(chosen) == M:
        print(" ".join(map(str, chosen)))
        return
    for i in range(N):
        chosen.append(li[i])
        generate(chosen)
        chosen.pop()
generate([])