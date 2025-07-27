import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1284_input.txt", "r")

T = int(input())

def getA(P, W):
    return P * W

def getB(Q, R, S, W):
    if W <= R: return Q 
    else: 
        return Q + (W-R) * S

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    A = getA(P, W)
    B = getB(Q, R, S, W)
    
    if A < B: print(f"#{test_case} {A}")
    else: print(f"#{test_case} {B}")
    