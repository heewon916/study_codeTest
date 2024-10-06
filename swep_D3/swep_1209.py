import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1209_input.txt", "r")

T = 10

for jc in range(1,T+1):
    testcase = int(input())
    
    num_maze = [] 
    for i in range(100):
        num_maze.append(list(map(int, input().split())))

    tmp_list = []
    for row in num_maze:
        tmp_list.append(sum(row))
        
    for col in list(zip(*num_maze)):
        tmp_list.append(sum(col))
    
    tmp_sum = 0
    for i in range(100):
        tmp_sum += num_maze[i][i]
    tmp_list.append(tmp_sum) 

    tmp_sum = 0 
    for i in range(100):
        tmp_sum += num_maze[100-i-1][i]
    tmp_list.append(tmp_sum)
    tmp_set = set(tmp_list)
    max_num = max(tmp_set)
    
    print('#{} {}'.format(testcase, max_num))