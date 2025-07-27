import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1217_input.txt", "r")

T = 10
def power(N, M):
    if M == 0: 
        return 1
    elif M % 2 == 0: 
        return power(N*N, M//2)
    elif M % 2 != 0: 
        return N * power(N*N,M//2)
    
for jc in range(1,T+1):
    # N의 M승
    # 거듭제곱을 재귀호출을 이용해 구현 
    
    testcase = int(input())
    N, M = map(int, input().split())
    
    print("#{} {}".format(testcase, power(N, M)))
        
            
        