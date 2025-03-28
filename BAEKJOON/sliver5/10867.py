N = int(input())
li = list(set(list(map(int, input().split()))))
li.sort()
for c in li: 
    print(c, end=' ')