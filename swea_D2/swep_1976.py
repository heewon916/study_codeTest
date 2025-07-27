#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    ans_h = (h1 + h2) % 12 
    ans_m = (m1 + m2) % 60
    if (m1 + m2) // 60: # 포인트 !!
        ans_h += (m1+m2) // 60
    print(f'#{test_case} {ans_h} {ans_m}')