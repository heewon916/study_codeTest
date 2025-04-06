import sys
input = sys.stdin.readline
N = int(input())
# 상근이가 갖고 있는 카드
Nl = list(map(int, input().split()))
M = int(input())
# 확인의 기준
Ml = list(map(int, input().split()))

# 이중반복문은 불가능
#Ml을 기준으로 Nl에 있는 숫자들을 확인해야 한다.
# 갖고 있는 카드를 오름차순으로 정렬하고
Nl.sort()
Ndic = {}
# 갖고 있는 카드들을 cnt 센다.
for n in Nl:
    if n in Ndic: Ndic[n] += 1
    else: Ndic[n] = 1

# 이때 Ml의 각 원소에 대해서
# Nl에 해당 원소가 있는지 이진 탐색을 수행한다.
# 있다면 Ndic의 값을 도출하고 없다면 0을 도출한다.

def binarySearch(m):
    low = 0
    high = len(Nl)-1
    while low <= high:
        mid = (low + high) // 2
        if Nl[mid] == m: return Ndic[m]
        elif Nl[mid] < m: low = mid + 1
        elif Nl[mid] > m: high = mid - 1
    return 0

for m in Ml:
    print(binarySearch(m), end=' ')