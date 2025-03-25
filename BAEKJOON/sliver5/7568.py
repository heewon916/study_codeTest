# (x,y) (p,q) => x>p and y>q 일때만 덩치가 더 크다
# 덩치 등수 = 자신보다 더 "큰 덩치"를 가진 사람의 명수
# 나보다 큰 덩치가 k명이면, 나는 k+1등이다. 

n = int(input())
li = []
for i in range(n):
    x,y = map(int, input().split())
    li.append((x,y))
    
for i in range(n):
    w, h = li[i]
    k = 0
    for j in range(n):
        if li[j][0] > w and li[j][1] > h: 
            k += 1
    print(k+1, end=' ')