# 기다리는 시간을 최소로 만들어야 한다.
# 소요시간을 오름차순으로 해서, 소요시간이 짧은 시간이 앞으로 오도록 한다.
import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
li.sort()
if N > 1:
    wait = 0
    total = 0
    for i in range(N):
        wait = sum(li[:i+1])
        total += wait
    print(total)
    # res = [0]*len(li)
    # res[0] = li[0]
    # res[1] = li[0] + li[1]
    # for i in range(1, N):
    #     res[i] = res[i-1] + li[i]
    # print(sum(res))
else:
    print(li[0])