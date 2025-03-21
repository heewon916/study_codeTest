for ts in range(int(input())):
    li = list(map(int, input().split()))
    n = li.pop(0)
    avg = sum(li)/n
    # print(n, avg, li)
    cnt = 0 
    for score in sorted(li, reverse=True):
        if score > avg: cnt += 1
    print('{}%'.format(round(cnt/n,5)*100))
        