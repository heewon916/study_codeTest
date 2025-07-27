import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1979_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # N = NxN퍼즐, K 길이의 문자열
    N, K = map(int, input().split())
    
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
        
    answer = 0 
    # 흰색 부분이 1 검은색 부분이 0 
    for i in range(N):
        cnt = 0 
        for j in range(N):
            if arr[i][j] == 1: # 가로로 체크 
                # print(f"arr[{i}][{j}] == 1", end=' ')
                cnt += 1
            else: 
                if cnt == K: 
                    answer += 1
                    break 
                else: cnt = 0 
        if cnt == K:
            answer += 1
        print(f'answer = {answer}')
        print()
    
    for j in range(N):
        cnt =0 
        for i in range(N):
            if arr[i][j] == 1: #연달아서 추가 필요 -> 인덱싱 사용하면 되지 않을까 
                # print(f"arr[{i}][{j}] == 1", end=' ')
                cnt += 1
            else: 
                if cnt == K: 
                    answer += 1  
                    break 
                else: cnt = 0 
        if cnt == K: 
            answer += 1        
        print(f'answer = {answer}')
        print()
        
    print(f'#{test_case} {answer}')
    
    # ///////////////////////////////////////////////////////////////////////////////////