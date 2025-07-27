import sys
sys.stdin = open("C:/study_codeTest/swep_D3/swep11315_input.txt", "r", encoding='UTF8')

T = int(input())

# 가로 세로 대각선 중 하나의 방향으로 5개 이상 연속한지 
for jc in range(1,T+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(str, input())))
    
    flag = False
    # 가로 체크 
    for i in range(N):
        tmp = ''.join(graph[i])
        if 'ooooo' in tmp:
            flag = True 
            print("가로 성공")
            break 
            
    # 세로 체크 
    if not flag:
        graph = list(zip(*graph))
        for i in range(N):
            tmp = ''.join(graph[i])
            if 'ooooo' in tmp:
                flag = True 
                print("세로 성공")
                break 
                
                
    # 대각선 체크 
    if not flag: 
        # tmp1 = 0
        tmp1 = []
        for i in range(N):
            tmp1.append(graph[i][i])
        if 'ooooo' in ''.join(tmp1):
            flag = True
            print("대각선 성공")
            #if graph[i][i] == 'o': 
            #    tmp1 += 1
            #elif graph[i][i] != 'o' and 1<= tmp1 < 5: 
            #   break 
            #if tmp1 == 5: # 연속적으로 쭉 잘 오면 
            #   flag = True 
                #print("대각선 성공")
            #    break 
             
            
    if not flag: 
        #tmp2 = 0
        tmp2 = []
        for i in range(N):
            tmp2.append(graph[i][N-i-1])
        if 'ooooo' in ''.join(tmp2):
            flag = True
            print("대각선 성공") 
            #if graph[i][N-i-1] =='o': 
            #    tmp2 += 1
            #elif graph[i][N-i-1] != 'o' and 1<= tmp2<5:
            #    break 
            #if tmp2 == 5: 
            #    flag = True 
                #print("대각선 성공")
            #    break 
            
            
    if flag: print(f"#{jc} YES")
    else: print(f"#{jc} NO")

                
                
    
