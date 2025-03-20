# 11:35 start 56 end
# dfs..
def dfs(i, total, result, cnt):
    global answer
    if cnt == 7:
        if total == 100 :
            answer = result
            return
    if i == 9:
        return # cnt = 7 이지만 100이 아니면 멈춰야 해
    #i 포함 X
    dfs(i+1, total, result, cnt)
    #i 포함 O
    dfs(i+1, total+nums[i], result+" "+str(nums[i]), cnt+1)
from itertools import combinations
nums = []
answer = ""
for _ in range(9):
    nums.append(int(input()))

# dfs(0, 0, "", 0)
for l in combinations(nums, 7):
    if sum(l) == 100:
        for i in l: print(i)
for i in answer.split():
    print(i)


