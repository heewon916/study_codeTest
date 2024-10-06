T = int(input("N 개수 입력:")) 
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    nums = list(map(int, input().split()))
    nums.sort()
    mid = len(nums) // 2
    print(nums[mid])