import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1966_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    numL = list(map(int, input().split()))
    numL.sort()
    print(f"#{test_case} ")
    for i in numL:
        print(i, end=' ')
    print()
    