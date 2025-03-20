import sys

# N = int(input())
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# 산술평균
print(int(round(sum(arr)/len(arr), 0)))
# 중앙값
arr.sort()
print(arr[N//2])
# 최빈값
ans = {}
# for i in list(set(arr)):
#     #n = arr.count(i) -> count 함수 시간복잡도 o(n)
#     #ans[i] = n
for i in arr:
    if i in ans: # keys() 는 시간복잡도 o(1)
        ans[i] += 1
    else:
        ans[i] = 1

# ans = dict(sorted(ans.items(), key=lambda x:x[1], reverse=True))
# max_n = []
# tmp = 0
# for k,v in ans.items():
#     if tmp <= v:
#         tmp = v
#         max_n.append(k)
#     else:
#         break
mx = max(ans.values()) #빈도수 중 최댓값 찾기
max_n = []
for i in ans.keys():
    if mx == ans[i]:
        max_n.append(i)
print(max_n[1] if len(max_n)>1 else max_n[0])
# 범위
# print(arr[-1] - arr[0])
print(max(arr) - min(arr))
