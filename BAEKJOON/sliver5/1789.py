import sys
input = sys.stdin.readline 

s = int(input())

# 서로 다른 n개의 자연수 ; 연속일수도 아닐수도
# 최대한 많은 자연수가 필요해 
i = 1
while True: 
    total = i*(i+1) // 2
    if total > s: 
        break 
    # print(i, total)
    i += 1
print(i-1)