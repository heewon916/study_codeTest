import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1215_input.txt", "r")

T = 10

def checkPalin(tmp_list, N):
        for i in range(N // 2):
            if tmp_list[i] != tmp_list[N-i-1]:
                return False
        return True
 
for jc in range(1,T+1):
    N = int(input()) # 찾아야 하는 회문의 길이 
    palinCount = 0 # 한 배열 안에서 회문의 개수 
    
    # 문자열 배열 가져오기 
    # 한 줄씩 들어오는 걸 8번 하면 된다 
    char_maze = [] 
    for i in range(8):
        char_maze.append(list(map(str, input())))
    
    # 행 먼저 체크하기 
    for row in char_maze: 
        for i in range(0, 8-N+1):
            tmp_list = row[i:i+N]
            if checkPalin(tmp_list, N):
                palinCount += 1
                
    # 열 그 다음으로 체크해야 됨 
    for col in list(zip(*char_maze)):
        for i in range(0, 8-N+1):
            tmp_list = col[i:i+N]
            if checkPalin(tmp_list, N):
                palinCount += 1
    print('#{} {}'.format(jc, palinCount))
    