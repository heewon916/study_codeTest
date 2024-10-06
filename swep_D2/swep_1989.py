import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1989_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    lit = input()
    litL = len(lit)
    ans = 1
    for i in range(litL):
        pt = litL - 1 - i
        if i <= pt and lit[i] != lit[pt]:
            ans = 0
    print(f"#{test_case} {ans}")
    # ///////////////////////////////////////////////////////////////////////////////////