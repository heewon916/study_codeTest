graph = [[0]*101 for _ in range(101)]
count = 0
for _ in range(int(input())): 
    y, x = map(int, input().split())  # y col x row 
    for i in range(x, x+10):
        for j in range(y, y+10):
                graph[i][j] = 1
for k in range(100):
    count += graph[k].count(1)

print(count)