'''
ord(문자): 아스키코드를 반환해준다 
chr(숫자): 숫자에 맞는 아스키코드를 반환해준다. 
'''
import sys
sys.stdin = open("swep2050_input.txt", "r")

#T = int(input())
T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    string = input()
    start_ascii = ord('A')-1
    for chr in string:
        print(ord(chr)-start_ascii, end=" ")
    # ///////////////////////////////////////////////////////////////////////////////////