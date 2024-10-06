import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1860_input.txt", "r")

T = int(input())

for jc in range(1,T+1):
    people, sec, bread = map(int, input().split())          # N명의 사람 예약/ M초에 K개 생산
    arriveList = sorted(list(map(int, input().split())))    # 도착하는 시간대 나열해둠: 같은 시간에 여러명 올 수 있다.
    
    prepared_bread = 0 
    state = "Possible"
    # time = 0 
    last_arrive = arriveList[-1]
    for time in range(last_arrive+1):
        if time != 0 and time % sec == 0: 
            prepared_bread += bread
            
        if time in arriveList: 
            prepared_bread -= 1
            if prepared_bread < 0: 
                state = "Impossible"
                break 
    print(f"#{jc} {state}")
    # while people != 0:
    #     if time != 0 and time % sec == 0:   # 0초 이후로 sec의 배수일때 K개 빵 생산됨 
    #         prepared_bread += bread
    #         print('time = {} prep_b ={}'.format(time, prepared_bread))
                
    #     if time in arriveList:            # 해당 time에 도착한 사람에 대해서
    #         print('time:{}'.format(time))
    #         prepared_bread -= 1
    #         people -= 1
    #         if prepared_bread < 0:      # 1. 준비된 빵이 있다면
    #             state = "Impossible"
    #             print('\tprep_bread{} people{}'.format(prepared_bread, people))
    #     time += 1
        
    print(f"#{jc} {state}")