# import sys
# sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1874_input.txt", "r")

# 해결은 했으나 답 베껴씀 

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dx = [0, 1, 0, -1]
dy = [1, 0 ,-1, 0]

for test_case in range(1, T + 1):
    N = int(input()) # 달팽이 
    
    maze = [[0 for y in range(N)] for x in range(N)]
    
    x, y = 0, 0 
    cnt = 1
    d = 0 
    
    for _ in range(N * N):
        maze[x][y] = cnt
        
        nx, ny = x + dx[d], y + dy[d]
        
        if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == 0: 
            x, y = nx, ny 
        else: 
            d = (d+1) % 4
            x, y = x + dx[d], y + dy[d]
        cnt += 1
    print(f"#{test_case}")
    for row in maze:
        print(" ".join(map(str, row)))
