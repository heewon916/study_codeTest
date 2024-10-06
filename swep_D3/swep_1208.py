import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1208_input.txt", "r")

T = 10
for jc in range(1,T+1):
    dump_cnt = int(input())
    box_hList = list(map(int, input().split()))
    
    for _ in range(dump_cnt):
        max_boxH = max(box_hList)
        max_boxH_idx = box_hList.index(max_boxH)
        
        min_boxH = min(box_hList)
        min_boxH_idx = box_hList.index(min_boxH)
        
        # print(box_hList)
        # print(max_boxH, max_boxH_idx)
        # print(min_boxH, min_boxH_idx)    
        box_hList[max_boxH_idx] -= 1 
        box_hList[min_boxH_idx] += 1 
        # print(box_hList)
        
    max_boxH = max(box_hList)
    min_boxH = min(box_hList)
    print(f"#{jc} {max_boxH - min_boxH}")