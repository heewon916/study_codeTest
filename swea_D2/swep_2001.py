import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep2001_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = input().split(' ')
    N = int(N); M = int(M)
    #print(N, M)
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split(' '))))
    #print(arr)
    sumL = []
    for i in range(N-(M-1)):
        for j in range(0, N-(M-1)):
            tmp = 0 
            for k in range(M): 
                tmp += sum(arr[i+k][j:j+M])
            sumL.append(tmp)        
    answer = max(sumL)
    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////