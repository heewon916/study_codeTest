# import sys
# sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1874_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 거슬러 줘야 할 금액 
    
    moneyL = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # answerL = {}
    # for i in range(8):
    #     answerL[moneyL[i]] = 0
    ansL = []
    for i in range(8):
        # answerL[moneyL[i]] = N // moneyL[i] 
        ansL.append(N // moneyL[i]) 
        N = N % moneyL[i]
    print(f"#{test_case}")
    for i in range(8):
        print(ansL[i], end=' ')
    print()