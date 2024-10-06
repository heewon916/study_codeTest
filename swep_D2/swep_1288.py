import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1288_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    k = 1 
    ansL = [x for x in range(0,10)]
    numL = []
    
    while len(numL) < 10: 
        # print(f"N = {N} k = {k}")
        for n in list(map(int, str(k*N))):
            # print(f"\tn = {n}", end=' ')
            if n not in numL: 
                numL.append(n)
                # print(f"numL.append({n})")
        # print(f"numL = {numL}")
        k += 1
    print(f"#{test_case} {N*(k-1)}") 
    # --> 몇번 세었을 까 가 아니라 마지막에 센 양의 숫자를 출력하는 문제 입니다.
    # --> 1로 시작하면 1...10이 되었을때 마지막에 본 양이 10이여서 10이정답인거지 10번 세어서 10이 아닙니다.
    # print()
        
    