import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep2805_input.txt", "r")

T = int(input())
for jc in range(1,T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input())))
    # print(maze)
    mid = N // 2
    total = sum(maze[mid][:]) 
    cnt = 0
    for row in range(mid-1, -1, -1): 
        cnt += 1
        tmp = sum(maze[row][cnt: N-cnt])
        # print(f"tmp = sum(maze[{row}][{cnt}: {N-cnt}])")
        total += tmp
        
    cnt = 0  
    for row in range(mid+1, N):
        cnt += 1
        tmp = sum(maze[row][cnt: N-cnt])
        # print(f"tmp = sum(maze[{row}][{cnt}: {N-cnt}])")
        total += tmp
    print(f"#{jc} {total}")
    
    