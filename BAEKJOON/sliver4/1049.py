# N개의 줄 필요
# 6줄 패키지, 낱개씩
# 기타줄 브랜드M개, 각 브랜드에서 파는 6줄 패키지-낱개 가격
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
pkg_g = []
slice_g = []
for _ in range(M):
    pkg, sli = map(int, input().rstrip().split())
    pkg_g.append(pkg)
    slice_g.append(sli)

mp = min(pkg_g)
ms = min(slice_g)

print(min(mp*(N//6+1), mp*(N//6) + ms*(N%6), ms*N))