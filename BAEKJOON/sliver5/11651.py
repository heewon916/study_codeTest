li = []
for i in range(int(input())):
    x, y = map(int, input().split())
    li.append((x,y))
    
for xy in sorted(li, key=lambda x:(x[1], x[0])):
    print("{} {}".format(xy[0], xy[1]))