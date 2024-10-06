import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1228_input.txt", "r")

T = 10

for jc in range(1,T+1):
    N = int(input())    # 원래 암호문 길이 10~20
    default_N = list(map(int, input().split()))    # 원래 문자열
    
    M = int(input())    # 명령어 개수 
    M_list = list(map(str, input().split('I')))
    for i in M_list:
        if len(i) > 1:
            print('i = {}'.format(i))
            # print(i.split(maxsplit=2))
            x, y, toAdd = i.split(maxsplit = 2)
            print('x={} y={} add={}'.format(x, y, toAdd))
    # x의 위치 바로 다음에 y개의 숫자를 입력 (y개의 숫자 s)
    