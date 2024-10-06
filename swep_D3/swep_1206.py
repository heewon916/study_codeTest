import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1206_input.txt", "r")

T = 10
for jc in range(1,T+1):
    building_cnt = int(input())
    building_h = list(map(int, input().split()))
    available = 0     
    for i in range(2, building_cnt-2):
        tmp_list = building_h[i-2:i+3]
        tmp_list.remove(building_h[i])

        max_heigh = max(tmp_list)
        # print(max_heigh, building_h[i])
        if building_h[i] > max_heigh:
             available += building_h[i] - max_heigh
            #  print(f"available = {available}")
    print(f"#{jc} {available}")
