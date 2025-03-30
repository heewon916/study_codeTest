# 1: 1 1 0 1등
# 2: 0 1 0 2등
# 3: 0 1 0 2등
# 4: 0 0 0 4등 

N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]
# 금은동 순으로 내림차순 정렬
medals.sort(key=lambda x:(x[1], x[2], x[3]), reverse = True)

# 국가 넘버 중 K값의 위치 인덱스 찾기 
idx = [medals[i][0] for i in range(N)].index(K)

# 해당 인덱스와 메달 수가 동일한 국가를 찾아 해당 인덱스 + 1
for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break 


# ### 100점 중 8점 풀이 
# N, K = map(int, input().split())
# li = []
# for _ in range(N):
#     state, a, b, c = map(int, input().split())
#     li.append([state, ''.join(map(str, [a,b,c]))])
# li.sort(key=lambda x:(x[1]), reverse=True)
# print(li)
# rank = 1
# max_ = li[0][1]
# # print('300'>'020', '010'>'001', '01')
# for i in range(1,N):
#     c, score = li[i]
#     if max_ == score: 
#         pass
#         # rank pass 
#     elif max_ > score: 
#         rank += 1
#         max_ = score
#     if K == c: 
#         print(rank)
#         break 
        