li = []
total = 0
for i in range(8):
    li.append((i+1,int(input())))
    
li.sort(reverse=True, key=lambda x:x[1])
li = sorted(li[:5], key=lambda x:x[0])
for c in li: 
    total += c[1]
print(total)
for c in li: 
    print(c[0], end=' ')