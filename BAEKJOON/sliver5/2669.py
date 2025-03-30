arr = [[0]*101 for _ in range(101)]
for i in range(4):
    x, y, a, b = map(int, input().split())
    # x, a는 열 y,b는 행
    # print("about {},{} and {},{}".format(x,y,a,b))
    for k in range(y, b): # b+1 -> b : 좌표가 아니라 박스를 구한다.
        for v in range(x, a):
            if arr[k][v] != 1: 
                arr[k][v] = 1
                # print(k, v)
total = 0
for i in range(101):
    # print(''.join(map(str, arr[i])))
    total += arr[i].count(1)
print(total)