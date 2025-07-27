import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1234_input.txt", "r")

T = 10
def makePw():    
    # 함수로 배열 넘겨서 그 안에서 처리할 때 
    # global을 사용해야 main의 배열에도 적용이 되더라 
    global pwList
    for i in range(len(pwList)-1):
        count = 0 
        if pwList[i] == pwList[i+1]:
            pwList = pwList[:i] + pwList[i+2:]
            count += 1
            # print('count: {} pwList:{}'.format(count, pwList))
            break
    if count:
        makePw()
    #elif count == 0 :
        #print('return pwList', pwList)
        # return pwList
            
for jc in range(1,T+1):
    N, pwInt = map(int, input().split())
    pwList = list(map(int, str(pwInt))) # 숫자는 non-iterable: pwInt => str(pwInt)
    # pwStr = str(pwInt)
    # 이웃한 숫자
    # 값이 같은 경우에만 소거된다. 
    # 정답 리스트를 따로 만드는 게 나을 듯 - 스택처럼? 
    # print(makePw(pwList)
    makePw()
    print('#{} {}'.format(jc, int(''.join(map(str, pwList)))))
    
        
            
    