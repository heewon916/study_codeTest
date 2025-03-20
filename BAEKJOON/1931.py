import sys
input = sys.stdin.readline
# from collections import deque

n = int(input())
# times = deque()
times = []
for _ in range(n):
    times.append(tuple(map(int, input().split())))
##########
# 아이디어를 떠올린다.
# 1. 시작 시간 기준으로 정렬
# print(sorted(times))
# 2. 종료 시간 기준으로 정렬 - 답
# print(sorted(times, key=lambda x:x[1])
# times = deque(sorted(times, key=lambda x:x[1]))
# times.sort(key=lambda x:(x[1], x[0]))
print(sorted(times, key=lambda x:(x[1], x[0])))
## ==> times.sort(key=lambda x:x[1]) 의 차이는 뭔가
print(sorted(times, key=lambda x:x[1]))
# print(times)
end_t = 0
cnt = 0
# while times:
#     s, e = times.popleft()
#     if end_t <= s:
#         cnt += 1
#         end_t = e
#         #print('checked', s, e)
#     elif end_t > s:
#         continue
for s, e in times:
    if end_t <= s:
        cnt += 1
        end_t = e

print(cnt)