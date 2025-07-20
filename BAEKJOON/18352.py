import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/1868_input.txt", 'r')  

T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(str, input())) for _ in range(N)]
    # print(mat)
    count_mat = [[-1]*(N) for _ in range(N)]
    dm = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    def find(i,j):
        count = 0 
        for m in dm: 
            dr, dc = m
            if 0<=dr+i<N and 0<=dc+j<N:
                if mat[dr+i][dc+j]=="*":
                    count += 1
        return count 

    # 1. 지뢰 갯수 세기
    for i in range(N):
        for j in range(N):
            if mat[i][j] == ".":
                count_mat[i][j] = find(i, j)
            else:
                count_mat[i][j] = "*" 

    # 2. 0인 곳 찾아서 click++
    click = 0 
    for i in range(N):
        for j in range(N):
            if count_mat[i][j] == 0: 
                click += 1
                for m in dm: 
                    nr, nc = i+m[0], j+m[1]
                    if 0<=nr<N and 0<=nc<N:
                        count_mat[nr][nc] = '*'
    for i in range(N):
        for j in range(N):
            if count_mat[i][j] != "*" and count_mat[i][j] != 0: 
                click += 1
    print("#{} {}".format(t, click))