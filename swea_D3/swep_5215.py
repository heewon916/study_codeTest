import sys
from itertools import combinations
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep5215_input.txt", "r")

T = int(input())
for jc in range(1,T+1):
    N, caloriLimit = map(int, input().split())
    
    table = {}
    for _ in range(N):
        grade, calory = map(int, input().split())
        table[grade] = calory 
        
    # 몇 개의 재료든 점수 높을수록 
    # 전체 칼로리는 caloriLimit 이하이기만 하면 된다. 
    
    # 재료 n개 선택
    # 재료 n-1개 선택
    # 재료 n-2개 선택
    # .. 재료 1개 선택 
    # => 최대한 많은 재료를 사용해야 한다. 
    # => 매회차에서 점수가 제일 높다고 판단되는 조합끼리 묶기
    
    def dfs(index, sTaste, sKcal):
        global maxTaste
        
        # 총 칼로리를 넘으면 리턴
        if sKcal > L:
            return
            
        # taste의 합이 제일큰 taste 합보다 크면 갱신
        if maxTaste < sTaste:
            maxTaste = sTaste
            
        # 햄버거 재료 데이터를 다 돌면 리턴
        if index == N:
            return
            
        # index 파라미터를 통해 taste, kcal 대입
        taste, kcal = data[index]
        
        # 햄버거 재료 리스트에서 재료를 사용했을 때
        dfs(index + 1, sTaste + taste, sKcal + kcal)
        # 햄버거 재료 리스트에서 재료를 사용하지 않았을 때
        dfs(index + 1, sTaste, sKcal)

    t = int(input())
    for tc in range(1, t+1):
        # N: 햄버거 재료 수, L: 넘지 말아야 하는 칼로리 양
        N, L = map(int, input().split())
        
        # 햄버거와 칼로리 리스트 저장
        data = [list(map(int, input().split())) for _ in range(N)]
        
        maxTaste = 0
        dfs(0, 0, 0)
        
        print("#{} {}".format(tc, maxTaste))
   
   
'''
DFS를 이용해 풀이하였음
햄버거 재료수(N), 넘지 말아야 하는 칼로리수(L)을 입력받고
리스트를 생성하고 재료의 맛과 칼로리를 저장한 후 

재료가 저장된 리스트의 인덱스 0 부터 끝까지 깊이 우선 탐색함.
탐색할때마다 칼로리가 넘어가면 탐색을 수행하지 않고
기존에 저장된 최대 맛보다 크면 갱신 과정을 거침 

재료를 썼을 때, 안 썼을 때 를 각각 탐색함.
'''
     
'''
    max_grade = 0
    max_index = 0  
    max_calori = 0 
    for n in range(N, -1, -1):
        grade_tble = list(combinations(table.keys(), n))
        calori_tble = list(combinations(table.values(), n))
        # print(f"grade_tble = {grade_tble}")
        # print(f"calori_tble = {calori_tble}")
        # print(f"sum(list(calori_tble[0])) = {list(calori_tble[0])}")
        # print(f"sum(list(calori_tble[0])) = {sum(list(calori_tble[0]))}")
        for i, grade in enumerate(grade_tble): 
            if max_grade < sum(list(grade)) and sum(list(calori_tble[i])) <= 1000: 
                max_grade = sum(list(grade)) 
                max_index = i
                max_calori = sum(list(calori_tble[i]))
            # print(f"max_grade = {max_grade} max_index = {max_index} max_calori = {max_calori}")
    print(f"#{jc} {max_grade}")
'''    

    
        
    