# N: ~2^7;
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0
def check_color(r, c, size):
    first_color = graph[r][c]
    for i in range(r, r+size):
        for j in range(c, c+size):
            if graph[i][j] != first_color:
                return -1
    return first_color

def divide(r, c, size):
    global blue, white
    if size == 1:
        if graph[r][c] == 1: blue += 1
        else: white += 1
        return

    color = check_color(r, c, size)
    if color == -1: # nothing
        mid = size // 2
        divide(r, c, mid)
        divide(r, c+mid, mid)
        divide(r+mid, c, mid)
        divide(r+mid, c+mid, mid)
    elif color == 1:
        blue += 1
    else:
        white += 1
divide(0, 0, N)
print(white)
print(blue)
