import sys
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
li = list(map(int, input().rstrip().split()))
li.sort()
count = 0
# 시간 제한: 2*10^8; N ~20개
def backtracking(idx, res):
    global count
    if idx == N:
        return
    if res+li[idx] == S:
        print(res, li[idx])
        count += 1
    backtracking(idx+1, res+li[idx])
    backtracking(idx+1, res)

backtracking(0, 0)
print(count)