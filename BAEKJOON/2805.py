import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    log = 0
    #print(start, end, mid, m)
    for t in tree:
        if t >= mid:
            log += t-mid
    if log > m:
        start = mid + 1
    elif log < m:
        end = mid - 1
    else:
        end = mid
        break
print(end)

################################################
# 시간 초과 코드
# arr.sort()
# low = 0
# high = len(arr)-1
# ans = 0
#
# while low<=high:
#     mid = (low + high) // 2
#     ans = arr[mid]
#     total = 0
#     for v in arr:
#         if arr[mid] < v: total += (v-arr[mid])
#     #print('total', total, 'm', m, 'mid:', ans)
#     if total < m: # 목표치 이하이면
#         high = mid - 1
#     elif total > m: # 목표치 이상이면
#         low = mid + 1
#     else:
#         break
# else:
#     while 1:
#         total = 0
#         for v in arr:
#             if ans < v: total += (v - ans)
#         if total > m: ans +=1
#         elif total == m: break
#
# print(ans)
