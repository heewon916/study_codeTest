import sys
N, M = map(int, input().split())
li = []
for i in range(N):
    li.append(list(map(str, input())))

# 시작점 (0,0) ~ (N-7, M-7)까지 살펴봐야 함
# 한 행에 대해서 흰색으로 시작하는 경우, 검정색으로 시작하는 경우
whitestart = 'WBWBWBWB'
blackstart = 'BWBWBWBW'
# int 타입의 양, 음의 무한대
res = sys.maxsize #양의 무한대
# res = float('inf')

# 각 시작점에 대해서
for i in range(0, N-7):
    for j in range(0, M-7):
        # i, j; 8x8 크기의 맨 왼쪽 상단 시작점 좌표
        startW = 0 # 맨 왼쪽 상단 시작점이 W인 경우, 변경이 필요한 곳을 카운트
        startB = 0 # 맨 왼쪽 상단 시작점이 B인 경우, 변경이 필요한 곳을 카운트
        for k in range(8):
            for l in range(8):
                if (k+l)%2==0: #짝수 행에 대해서
                    # 맨 좌측 상단이 W로 시작해야 하는 경우; 현재 B이면 변경 필요
                    if li[i+k][j+l] == "B": startW += 1
                    # 맨 좌측 상단이 B로 시작해야 하는 경우; 현재 W이면 변경 필요
                    if li[i+k][j+l] == "W": startB += 1
                else: # 홀수행은 짝수행과 반대로 처리하면 된다
                    if li[i+k][j+l] == "W": startW += 1
                    if li[i+k][j+l] == "B": startB += 1
        res = min(res, startW, startB)
print(res)
            # if k%2 == 0:
            #     startW += sum([1 for a,b in zip(li[i], whitestart) if a !=b])
            #     startB += sum([1 for a,b in zip(li[i], blackstart) if a !=b])
            # else:
            #     startW += sum([1 for a,b in zip(li[i], blackstart) if a !=b])
            #     startB += sum([1 for a,b in zip(li[i], whitestart) if a !=b])
        # res.append(min(startW, startB))
# print(res, min(res))
