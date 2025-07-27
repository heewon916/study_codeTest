import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D2\\swep1946_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    input_list = {}
    for i in range(N):
        alphabet, num = map(str, input().split())
        input_list[alphabet] = int(num)
    
    print_list = [] 
    cnt = 0 
    
    for alphabet, num in input_list.items():
        for i in range(num):
            print_list.append(alphabet)
            cnt += 1
            input_list[alphabet] -= 1
            if cnt == 10: 
                cnt = 0 
                print_list.append('\n')
                # 왜 이렇게 복잡하게 해
                # print_list.append(alphabet*input_list[alphabet])
                # cnt += input_list[alphabet]
    print(f"#{test_case}")
    print(''.join(print_list))
                        
        
    
                    
    
            