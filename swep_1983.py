import sys
sys.stdin = open("C:/2024_CodeTest/swep_D2/swep1983_input.txt", "r")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    gradeL = {}
    # answerL = []
    evaluationL = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K = map(int, input().split())
    for i in range(N):
        mid, final, work = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + work * 0.2
        gradeL[i+1] = round(total,2)
    
    # 점수를 내림차순으로 정렬 
    gradeL = dict(sorted(gradeL.items(), key=lambda x:x[1], reverse = True))
    # print(gradeL)
    
    # 입력데이터에서 K번째 학생의 학점을 가져오기 
    # 1. gradeL에서 키값=K인 점수를 가진 그 학생이 내림차순에서 어디에 있는지 찾고
    for i, key in enumerate(gradeL.keys()):
        if key == K: 
            k = i # 평점에서는 k번째에 위치한 거니까 
            # print(i, k, gradeL[key], end=' ')
            break 
    # 2. evaluationL에서 인덱스 k에 해당하는 평점 찾으면 됨 
    # print(k // (N//10))
    print(f"#{test_case} {evaluationL[k//(N //10)]}")
    
    
    # ///////////////////////////////////////////////////////////////////////////////////