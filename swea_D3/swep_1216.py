import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1240_input.txt", "r")

T = 10 

def checkPalin(strlist, N):
    # N = len(strlist)
    for i in range(N//2):
        if strlist[i] != strlist[N-i-1]:
            return False
    return True


for jc in range(1,T+1):
    testcase = int(input())
    char_maze = [] 
    for _ in range(100):
        char_maze.append(list(map(str, input())))
    
    # 행과 열로 봤을 때 가장 길이가 긴 회문을 찾는 게 포인트 
    
    # 1. 일단 회문을 찾는다. 
    # - 이때 N의 길이(회문의 길이)는 최대치에서부터 시작한다. 
    max_length = 0 
    
    for row in char_maze:
        for N in range(100, -1, -1):
            for i in range(100-N+1):
                tmp_list = row[i:i+N]
                if checkPalin(tmp_list, N):
                    length = len(tmp_list)
                    if length >= max_length: 
                        max_length = length
                        #print('tmp_list = {} max_length = {}'.format(tmp_list, max_length))
                        
    for col in list(zip(*char_maze)):
        for N in range(100, -1, -1):
            for i in range(100-N+1):
                tmp_list = col[i:i+N]
                if checkPalin(tmp_list, N):
                    length = len(tmp_list)
                    if length >= max_length: 
                        max_length = length
                        #print('tmp_list = {} max_length = {}'.format(tmp_list, max_length))
    # print("{} FINISHED".format(testcase))
    print('#{} {}'.format(testcase, max_length))
    
    
    # 2. 해당 회문의 길이를 max와 비교한다. 
    # 3. 해당 회문의 길이 > max 이면 업데이트한다. 