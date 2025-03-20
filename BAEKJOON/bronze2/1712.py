a,b,c= map(int, input().split())

if b== c or (a/(c-b)) < 0: 
    print(-1)
else:
    # n = 1
    # while (a+b*n) >= c*n:
    #     n += 1
    # print(n)
    print(int(a/(c-b))+1)