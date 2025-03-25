li = []
for i in range(int(input())):
    x, y = map(int, input().split())
    li.append((x,y))

for i in sorted(li, key=lambda x:(x[0], x[1])):
    print(i[0], i[1])
