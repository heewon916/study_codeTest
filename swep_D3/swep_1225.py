import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1225_input.txt", "r")

T = 10

def makeCode(nums):
    for i in range(1, 6): #0부터 7을 빼는 게 아니라 1부터 5까지만 뺀다는 걸 그림보고 알아차렸어야 해.
        nums[0] = nums[0] - i 
        first = nums.pop(0)
        nums.append(first)
        # 0보다 작아지거나 0일 경우 0으로 저장되면, 프로그램은 종료된다. 
        if first <= 0: 
            nums[7] = 0
            # break 
            return True
        
   #  print('i: {} nums:{}'.format(i, nums))

for jc in range(1,T+1):
    testcase = int(input())
    nums = list(map(int, input().split()))
    
    # 리스트에서 +1 >> remove >> append 반복 
    # 모두 한자리수가 되기까지 반복: // 10 했을 때 0이어야 함. 
    
    # print('start: {}'.format(nums))
    while True:
        if makeCode(nums):
            break

    print('#{} {}'.format(testcase, ' '.join(map(str, nums))))
    
        
        
        