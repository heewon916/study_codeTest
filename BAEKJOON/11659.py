import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
t = [0]
tmp = 0
for n in arr:
    tmp = tmp + n
    t.append(tmp)
# print(t)
for _ in range(m):
    i, j = map(int, input().split())
    print(t[j] - t[i-1]) #0부터 저장하면, t[j-1]-t[i-2]인데, i=1일 때 인덱스 에러가 뜬다. 안됨
    # print(sum(arr[i-1:j]))
    # total = 0
    # for v in range(i-1, j):
    #     total += arr[v]
    # print(total)
