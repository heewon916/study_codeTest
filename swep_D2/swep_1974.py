import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1974_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def checkS(arr):
    # 3x3 
    rowL = []
    colL = [] 
    for r in range(9):
        for c in range(9):
            # 3x3
            if r%3 == 0 and c%3 == 0: # 0,3,6
                # print(f"r = {r} c = {c}")
                numL = []
                for i in range(3):
                    for j in range(3):
                        numL.append(arr[r+i][c+j])
                # print(f"numL = {numL}")
                numL.sort() 
                for i in range(1,10): # 1~9 
                   if i != numL[i-1]: 
                    #    print("3x3 no")
                       return 0
                numL.clear() 
            # row and col check 
            rowL.append(arr[r][c])
            colL.append(arr[c][r])
        # print(f"r = {r} c = {c} -> rowL = {rowL}")
        # print(f"r = {r} c = {c} -> colL = {colL}")
        rowL.sort() 
        colL.sort()
        for i in range(1,10):
            if i != rowL[i-1] or i != colL[i-1]: 
                # print("row and col no")
                return 0 
        rowL.clear() 
        colL.clear()
    return 1

for test_case in range(1, T + 1):
    # 조건은 3가지 1. 3x3 2. 가로줄 3. 세로줄 
    # 모든 숫자는 1~9 정수 
    
    # 일단 입력값 넣고 
    arr = []
    for i in range(9):
        arr.append(list(map(int, input().split())))
        
    # 조건 모두 확인하는 함수 호출 
    print(f"#{test_case} {checkS(arr)}")