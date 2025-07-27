import sys
sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep2817_input.txt", "r")

T = int(input())

def dfs(i, result):
    global count 
    if result == K: # 원하는 결과가 나왔거나 
        count += 1
        return 
    if i == N: # 인덱스 끝까지 봤거나 
        # 이 if문이 뒷순서여야 하는 이유: 마지막 인덱스를 봤는데 합이 K일 수 있잖아
        # 먼저 실행시키면 count가 증가가 안됨.
        return 
    dfs(i+1, result + nums[i])
    dfs(i+1, result)
    
for jc in range(1,T+1):
    N, K = map(int, input().split())
    # N개의 자연수가 주어지고 (값이 같아도 다른 걸로 인정)
    # 잘 조합해서 K가 되면 됨 (1개를 선택해도 된다)
    # =>> DFS 로 풀이할 수 있다. 
    nums = list(map(int, input().split()))
    count = 0 
    dfs(0, 0)
    print("#{} {}".format(jc, count))
    
    # max_combi = len(nums)
    # # 가장 적게 선택하는 것부터 해서 permutations 돌리기 
    # for i in range(1, max_combi+1):
    #     tmp_list = list(combinations(nums, i))
    #     for item in tmp_list:
    #         if K == sum(item):
    #             count += 1
    #             #print('i{} K{} == sum{}'.format(i, K, item))
   
    
    