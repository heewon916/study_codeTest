N = int(input())
li = [i for i in range(1, N+1)]

while len(li) > 1: 
    print(li.pop(0), end= ' ')
    v = li.pop(0)
    li.append(v)
print(li[-1])