N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

A, B, C = 0, 0, 0 # -1, 0, 1 개수

def chck(x, y, size):
    first_n = graph[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if first_n != graph[i][j]:
                return -2
    return first_n

def div_conq(x, y, size):
    global A,B,C
    res = chck(x, y, size)
    if res == -1:
        A += 1
        return
    elif res == 0:
        B += 1
        return
    elif res == 1:
        C += 1
        return
    else:
        new_size = size//3
        for nx in range(3):
            for ny in range(3):
                div_conq(x+nx*new_size, y+ny*new_size, new_size)

div_conq(0, 0, N)
print(A)
print(B)
print(C)