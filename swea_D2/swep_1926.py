#import sys
#sys.stdin = open("input.txt", "r")

#T = int(input())
T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 3,6,9가 들어간 수는 말하지 않고 박수 -> 3,6,9 들어있는 갯수만큼
    # 박수 표시: - 
    N = int(input()) # 1부터 N까지 369게임 
    for num in range(1, N+1):
        # 3,6,9가 들어간 숫자 
        numL = []
        for i in str(num):
            numL.append(i)
        # print(numL)
        cnt = 0; case = False
        for n in numL: 
            if n in ('3', '6', '9'):
                cnt+=1
                case = True
        if case: 
            print('-'*cnt, end=' ')
        else: 
            print(num, end=' ')
        # # 3,6,9가 안 들어간 숫자 
        # else: 
        #     print(i, end=' ')
    # ///////////////////////////////////////////////////////////////////////////////////
    
########################################################
# 다른 답안1
T = int(input())
arr = [str(i) for i in range(1, T+1)] #1부터 T까지 각 숫자를 전부 문자로 바꾸고 
print(arr)         
# 실행결과: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
for num in arr: #각 숫자에 대해서 
    cnt = 0 
    
    for tmp_num in num: # 한 숫자: 13이면 -> 1과 3에 대해  
        if int(tmp_num)%3 == 0 and int(tmp_num)!=0: # 그 숫자가 3으로 나누어떨어지면 3이 있는 거니까 
            cnt += 1
    if cnt > 0: #만약 cnt가 1이상이면
        for c in range(cnt): # cnt 횟수만큼 '-' 를 띄우지 않고 출력
            print('-', end='')
        print(end=" ") 
    else: # 만약 cnt가 0이면 3은 없단 뜻이니까
        print(int(num), end=" ")
        
# 다른 답안 2
N = int(input())

for i in range(1,N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        clap_count = str(i).count('3') + str(i).count('6') + str(i).count('9')
        print('-' * clap_count, end=' ')
    else:
        print(i, end=' ')