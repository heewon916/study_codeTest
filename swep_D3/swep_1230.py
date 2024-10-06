import sys
import re
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep1230_input.txt", "r")

T = 10    
    
for jc in range(1,T+1):
    N = int(input())    # 원래 암호문 길이 10~20
    default_N = list(map(int, input().split()))    # 원래 문자열
    M = int(input())    # 명령어 개수 
    M_list = re.split(r'([IAD])', input()) 
            
    for i in range(0, len(M_list)): 
        if M_list[i] == 'I':
            x,y,toAdd = M_list[i+1].split(maxsplit=2)
            x = int(x)
            toAddlist = list(map(int, toAdd.split()))
            default_N = default_N[:x] + toAddlist + default_N[x:]
        elif M_list[i] == 'D':
            x, y = M_list[i+1].split()
            x = int(x); y = int(y)
            default_N = default_N[:x+1] + default_N[x+y+1:]
        elif M_list[i] == 'A':
            x, toAdd = M_list[i+1].split()
            toAddlist = list(map(int, toAdd.split()))
            default_N = default_N + toAddlist
            
    print(f"#{jc} {' '.join(map(str, default_N[0:10]))}")   