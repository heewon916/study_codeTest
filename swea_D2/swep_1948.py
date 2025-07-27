import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1948_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    month1, day1, month2, day2 = map(int, input().split())
    
    lastdays_list = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    get_month_list = [] 
    for i in range(month1+1, month2):
        get_month_list.append(i)
    # print(get_month_list)
    
    daysLeft = lastdays_list[month1] - day1 + 1 
    
    for m in get_month_list:
        daysLeft += lastdays_list[m]
    
    if month1 != month2:
        daysLeft += day2 
    
    print(f"#{test_case} {daysLeft}")
    # ///////////////////////////////////////////////////////////////////////////////////