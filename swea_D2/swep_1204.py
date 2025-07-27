import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1204_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    test_case = int(input())
    grade_list = list(map(int, input().split()))
    
    grade_dict = {} 
    
    for num in grade_list: 
        if num in grade_dict.keys(): 
            grade_dict[num] += 1
        else: 
            grade_dict[num] = 1
    
    sort_gradeD = sorted(grade_dict.items(), key=lambda x: x[1], reverse=True)
        
    print(f"#{test_case} {sort_gradeD[0][0]}")
    