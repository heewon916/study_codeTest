import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
# 이 수들이 A안에 존재하는지 알아낸다.
mLi = list(map(int, input().split()))

# 100,000 이중 반복 시키면 10^10으로 1초 넘어감.
# 단 한번의 반복문 안에서 해결해야 한다.

inter = set(mLi).intersection(set(A))

for c in mLi:
    if c in inter:
        print(1)
    else:
        print(0)