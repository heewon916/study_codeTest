import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1244_input.txt", "r")

T = int(input())
for jc in range(1,T+1):
    N, switch_cnt = map(int, input().split())
    
    N_list = list(map(int, str(N)))
    changed_pt = 0
    for _ in range(switch_cnt):
        if N_list[changed_pt:]:
            get_max = max(N_list[changed_pt:])
            max_pt = N_list.index(get_max)
            print(N_list, get_max, max_pt)
            
            tmp = N_list[max_pt]
            N_list[max_pt] = N_list[changed_pt]
            N_list[changed_pt] = tmp 
            
            print(N_list)
            changed_pt += 1
    # print(N_list)
    # answer = "".join(map(str, N_list))
    # print(f"#{jc} {answer}")
    
    