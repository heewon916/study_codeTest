import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1984_input.txt ", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    numL = list(map(int, input().split()))
    #print(numL)
    maxi = numL.index(max(numL))
    mini = numL.index(min(numL))
    length = len(numL)
    #print(maxi, mini)
    if maxi == mini: 
        # del numL[maxi]
        numL[maxi] = 0 
        length -= 1
    else:
        # del numL[maxi]
        # del numL[mini]
        numL[maxi] = 0 
        numL[mini] = 0 
        length -= 2

    #print(numL)
    sum = 0 
    for i in numL:
        sum += i 
    numL_avg = round(sum/length)
    print(f"#{test_case} {numL_avg}")
    # ///////////////////////////////////////////////////////////////////////////////////