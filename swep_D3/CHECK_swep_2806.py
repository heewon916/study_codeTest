import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep2806_input.txt", "r")

T = int(input())

def dfs(row): 
    '''row 행에 퀸을 놓아보기'''
    global cnt 
    
    if row == N:                # 1. 퀸을 n행까지 조건에 맞게 다 채워넣은 경우
        cnt += 1                # => 마지막 행이라면 둘 수 있는 곳은 하나뿐이니까 탐색 끝남.
        
    else:                       # 2. 마지막 행이 아니면 반복해야 해
        for i in range(N):      
            rows[row] = i                   # (row, i)에 퀸 배치해보기 (일단)
            if is_valid(row):               # 공격을 안 받으면
                dfs(row + 1)                # row+1 행에서 반복 
                
                
                
def is_valid(row):
    '''현재 놓은 퀸 자리가 유효한지 체크해야 해'''
    
    for before_row in range(row):           # range(N)이 아니라 range(now_row)인 이유: 굳이 전체를 보기보다 여태 거쳐온 범위만 보는 게 효율적
        if rows[before_row] == rows[row]:   # 같은 열에 두는 경우
            return False 
        if abs(before_row-row) == abs(rows[before_row]-rows[row]):  # 대각선에 두는 경우
            return False 
        
    return True                             # 모두 해당되지 않으면 유효한 자리 


for jc in range(1,T+1):
    N = int(input())                # n x n & n개의 queen 놔야 함 
    
    rows = [0 for i in range(N)]    # rows[r] = c => r행에 c퀸이 놓여져 있음을 의미한다. 
    cnt = 0                         # 가능한 경우의 수 저장 
    dfs(0)                          # 0행부터 탐색 시작
    print('#{} {}'.format(jc, cnt))
    
                    
    
    
    
    
    
    
            