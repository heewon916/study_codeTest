import sys
sys.stdin = open("swep2056_input.txt", "r")
T = int(input())
valued_dayL = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
               7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# 여러개의 테스/트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////////////////////////
    longdate = int(input())
    year = longdate // 10000; longdate %= 10000
    month = longdate // 100; longdate %= 100
    day = longdate
    #print(year, month, day)
    if month >= 1 and month <= 12:
        #print(month, valued_dayL[month])
        if  day >= 1 and day <= valued_dayL[month]:
            #print(year, month, day, valued_dayL[month])
            print(f"#{test_case} {year:4d}/{month:2d}/{day:2d}")
        else: 
            print(f"#{test_case} -1")    
    else: 
        print(f"#{test_case} -1")
    
    # ///////////////////////////////////////////////////////////////////////////////////