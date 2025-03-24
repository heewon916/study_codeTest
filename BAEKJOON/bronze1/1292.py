a, b = map(int, input().split())
li = []
for i in range(1, 100):
    if len(li) == 1000: 
        break 
    for _ in range(i):
        li.append(i)

print(sum(li[a-1:b]))