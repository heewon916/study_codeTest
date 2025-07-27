import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1959_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A, B = [], []
    # A, B 
    if N <= M: 
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
    else: 
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))
    
    # move and multi 
    sumList = [] 
    
    for i in range(abs(N-M)+1):
        tmp = 0 
        for a in range(len(A)):
            # print(f'A[{a}]*B[{a+i}] = {A[a]}*{B[a+i]}')
            tmp += A[a]*B[a+i]
        sumList.append(tmp)
        # print(i, sumList)
    print(f"#{test_case} {max(sumList)}")
    # print()
    
            