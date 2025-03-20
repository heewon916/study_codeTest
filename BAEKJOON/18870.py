import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_set = sorted(list(set(arr)))

dic = dict()

# 문제 풀이 방법: 결국 정렬하면 인덱스 번호가 구하려는 cnt 값이다.
for i, v in enumerate(arr_set):
    dic[v] = i

for i in  arr:
    print(dic[i], end = ' ')

######## 시간 초과 코드
# for i in arr:
#     cnt = 0
#     for j in arr_set:
#         if i > j: cnt += 1
#         else: break
#     print(cnt, end=' ')
