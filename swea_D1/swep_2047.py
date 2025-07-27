import sys
sys.stdin = open("swep2047_input.txt", "r")

#T = int(input())
T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    headL = input() 
    #print(headL.upper())
    # A 65 ~ Z 90 
    # a 97 ~ z 122
    answer = []
    for char in headL: 
        if char >= 'a' and char <= 'z':
            char = chr(ord(char)-32)
            answer.append(char)
        else: 
            answer.append(char) 
    print(''.join(answer))
    # ///////////////////////////////////////////////////////////////////////////////////