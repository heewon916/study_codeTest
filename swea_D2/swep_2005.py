import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep2005_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input()) 
    arr = [[0 for j in range(N)] for i in range(N)]
    arr[0][0] = 1
    for i in range(0, N): # 0~N-1 => 1~ N-1
        for j in range(i+1): #0~i => 0 ~ N-1
            if j == 0: arr[i][j] = 1
            else: 
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            print(arr[i][j], end=' ')
        print()
    print()
    # ///////////////////////////////////////////////////////////////////////////////////