import sys
sys.stdin = open("C:/study_codeTest/swep_D3/swep6808_input.txt", "r", encoding='UTF8')
from itertools import permutations
T = int(input())

for tc in range(1,T+1):
    a_list = list(map(int, input().split()))
    b_list = [x for x in range(1,19) if x not in a_list]

    b_tc = list(permutations(b_list, len(b_list)))

    






