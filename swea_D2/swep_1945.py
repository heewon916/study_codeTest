import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1945_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    primeL = {2:0, 3:0 ,5:0 ,7:0 ,11:0}
    while N != 1: 
        # print(f"N = {N}")
        for p, n in primeL.items():
            while N%p == 0:
                primeL[p] += 1
                N = N // p
                # print(f"p = {p}  n = {n} N = {N}")
    print(f"#{test_case} ", end='')
    for v in primeL.values(): 
        print(v, end=' ')
    print() 
                