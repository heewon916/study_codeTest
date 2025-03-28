n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    i -= 1; j -=1; x-=1; y-=1
    total = 0 
    
    if i != x:
        # 처음 행
        total += sum(arr[i][j:])
        # 끝 행
        total += sum(arr[x][:y+1])
        # 중간 행
        for k in range(i+1, x):
            total += sum(arr[k][:])
        # row = i 
        # while True: 
        #     if row == x: 
        #         print("1 {}".format(arr[x][:y+1]))
        #         total += sum(arr[x][:y+1])
        #         break 
        #     elif row == i:
        #         print("2 {}".format(arr[row][j:]))
        #         total += sum(arr[row][j:])
        #     elif i < row and row < x:
        #         print("3 {}".format(arr[row][:]))
        #         total += sum(arr[row][:])
        #     row += 1
    else: 
        total = sum(arr[i][j:y+1])
    print(total)