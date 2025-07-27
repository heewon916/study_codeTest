import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1289_input.txt", "r")

T = int(input())

for jc in range(1,T+1):
    mem = list(map(int, input()))  # 정답 가져오기
    answer = [0 for i in range(len(mem))] # 원래는 000..0 
    # print(mem)
    # print(answer)
    
    # 원래 정답이 1이면 거기부터 일단 시작 
    # 그리고 원래 정답에서 이전과 현재값이 다르면 (1과 0) 현재값부터 세팅
    ptr = 1 
    cnt = 0 
    for i in range(len(mem)-1):
        if i == 0 and mem[i] == 1: 
            cnt += 1
        elif mem[i] == mem[ptr]:
            continue
        elif mem[i] == 1: 
            # answer[i:] = 1
            cnt += 1
        elif mem[i] == 0 :
            # answer[i:] = 0
            cnt += 1
        ptr += 1
            
    print('#{} {}'.format(jc, cnt))
            
