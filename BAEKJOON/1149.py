# N 1000 
# 인접한 부분끼리는 색이 달라야 한다. 
# 비용의 최솟값 구하기 

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

    # 