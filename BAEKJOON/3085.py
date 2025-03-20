# 2:27  start
def search():
    global answer
    # 가로, 세로로 가장 긴 연속 부분을 찾아야 함
    # 1. 행 쪽
    for i in range(N):
        cnt = 1 # 1로 시작해야 마지막까지 셀 수 있다.
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
                answer = max(answer, cnt)
            else:   # 연속을 찾아야 되는데, 중간에 끊기면 원상복구하고 다시 세기
                cnt = 1
        # answer = max(answer, cnt) 여기다가 두면, 도중에 끊겨서 1이 되어버리지

    # 2. 열 쪽
    for j in range(N):
        cnt = 1
        for i in range(N-1):
            if arr[i][j] == arr[i+1][j]:
                cnt += 1
                answer = max(answer, cnt)
            else:  # 연속을 찾아야 되는데, 중간에 끊기면 원상복구하고 다시 세기
                cnt = 1
        # answer = max(answer, cnt)

N = int(input())
arr = []
answer = 0
for _ in range(N):
    arr.append(list(map(str, input())))

#1. 색이 서로 다른 두 칸 교환해보기
for i in range(N):
    for j in range(N):
        if j+1 < N: # 가로끼리 바꿔보기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            search()
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j] # 원상복구
        if i+1 < N: # 세로끼리 바꿔보기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            search()
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]  # 원상복구
print(answer)