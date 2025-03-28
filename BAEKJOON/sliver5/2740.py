N, M = map(int, input().split()) #A
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
_, K = map(int, input().split()) #B
b = []
for i in range(M):
    b.append(list(map(int, input().split())))
    
c = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        res = 0
        for x in range(M):
            res += a[i][x]*b[x][j]
        c[i][j] = res 
for r in c: 
    print(" ".join(map(str, r)))