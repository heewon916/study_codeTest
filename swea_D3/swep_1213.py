import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1213_input.txt", "r", encoding='UTF8')

T = 10

for jc in range(1,T+1):
    testcase = input()
    toSearch = input() 
    string = input()
    
    count = 0 
    
    # 1. 찾고자 하는 문자열의 길이를 갖고 
    # 2. for문 돌리는 게 답일 것 같은데 
    
    N = len(toSearch)
    stringLen = len(string)
    
    for i in range(stringLen-N+1):
        tmpStr = string[i:i+N]
        if tmpStr == toSearch: 
            count += 1
            #print('count={} toSearch:{} tmpstr:{}'.format(count, toSearch, tmpStr))
        
    print('#{} {}'.format(testcase, count))
            
            