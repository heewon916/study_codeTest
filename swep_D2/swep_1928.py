import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1928_input.txt", "r")

T = int(input())
base64Table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for test_case in range(1, T + 1):
    string = input()
    tmp_binary = []
    for c in string: 
        tmp_binary.append(format(base64Table.index(c), 'b').zfill(6))
    tmp = ''.join(tmp_binary)
    # print(tmp_binary)
    asciiTable = [] 
    for i in range(0, len(tmp), 8):
        asciiTable.append(int(tmp[i:i+8], 2))
    
    answerL = [] 
    for n in asciiTable:
        answerL.append(chr(n))
    print(f"#{test_case} {''.join(answerL)}")
    
    