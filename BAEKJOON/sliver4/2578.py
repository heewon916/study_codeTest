# 하나의 수를 지울 때마다 빙고인지 확인해야 한다.

def chkBingo():
    global chk
    bingo = 0
    # 가로 빙고
    for row in chk:
        if row.count(1) == 5:
            bingo += 1
    # 세로 빙고
    for col in zip(*chk):
        if col.count(1) == 5:
            bingo += 1
    # 대각선 빙고
    if all(chk[i][i] == 1 for i in range(5)):
        bingo += 1
    if all(chk[i][4-i] == 1 for i in range(5)):
        bingo += 1
    return  bingo

arr = [list(map(int, input().split())) for _ in range(5)]
# 수를 부르면 0 -> 1 체크
chk = [[0 for i in range(5)] for _ in range(5)]
# 각 숫자가 위치하고 있는 빙고 판 좌표 (i,j)
dic = {}
for i in range(5):
    for j in range(5):
        dic[arr[i][j]] = [i, j]

# cnt; 몇 번째 수인지 확인
cnt = 0
for i in range(5):
    tmp = list(map(int, input().split()))
    for k in tmp:
        x, y = dic[k]
        chk[x][y] = 1
        cnt += 1
        if chkBingo() >= 3:
            print(cnt)
            # break
            exit()

