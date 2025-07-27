import sys
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep1228_input.txt", "r")

T = 10

for jc in range(1,T+1):
    N = int(input())    # 원래 암호문 길이 10~20
    default_N = list(map(int, input().split()))    # 원래 문자열
    M = int(input())    # 명령어 개수 
    M_list = list(map(str, input().split('I')))
    for i in M_list:
        if len(i) > 1:
            x, y, toAdd = i.split(maxsplit = 2)
            x = int(x)
            toAddList = list(map(int, toAdd.split()))
            default_N = default_N[:x] + toAddList + default_N[x:]
    
    print(f"#{jc} {' '.join(map(str, default_N[0:10]))}")
    