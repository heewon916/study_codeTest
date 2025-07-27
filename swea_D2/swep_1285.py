import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1285_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N_people = int(input())
    dist_list = list(map(int, input().split()))
    near_to_zero = 0 

    for i, dist in enumerate(dist_list): 
        dist_list[i] = abs(dist)

    get_min = min(dist_list)
    
    for dist in dist_list: 
        if get_min == dist: near_to_zero += 1
    
    print(f"#{test_case} {get_min } {near_to_zero}")
    
    