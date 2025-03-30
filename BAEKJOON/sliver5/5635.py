N = int(input())
li = []
for _ in range(N):
    name, d, m, y = map(str, input().split())
    d = int(d); m = int(m); y=int(y)
    li.append([name,(y,m,d)])
    
li.sort(key=lambda x:(x[1][0], x[1][1], x[1][2]))

print(li[-1][0])
print(li[0][0])
