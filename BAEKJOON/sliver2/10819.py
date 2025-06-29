from itertools import permutations
N = int(input())
arr = list(map(int, input().split()))

def getsum(arr):
    res = 0
    for i in range(N-1):
        res += abs(arr[i]-arr[i+1])
    return res
max_res = 0
for tmp in permutations(arr, N):
    max_res = max(getsum(tmp), max_res)
print(max_res)