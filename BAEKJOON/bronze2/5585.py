left = 1000 - int(input())
bkt = [500, 100, 50, 10, 5, 1]
i = 0 
cnt = 0 
while left > 0: 
    cnt += left // bkt[i]
    left = left % bkt[i]
    # print(bkt[i], cnt, left)
    i += 1
print(cnt)