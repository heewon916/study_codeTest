n = int(input())
set_n = set(list(map(int, input().split())))

m = int(input())
li_m = list(map(int, input().split()))

for i in li_m: 
    if i in set_n:
        print(1, end=' ')
    else:
        print(0, end=' ')

# for i in range(n):
#     if li_n[i] in set_m:
#         print(1, end=' ')
#     else: 
#         print(0, end=' ')


# li_m의 각 수에 대해서 li_n에 있는지 확인 
# 완전탐색 => 이중 반복 불가 
# 정렬? 각각 비교? 이진탐색? 힙트리.. 

# for i in li_m: 
#     if i in li_n: 
#         print(1, end=' ')
#     else: 
#         print(0, end=' ')