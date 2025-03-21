from itertools import combinations

li = []
for i in range(9):
    li.append(int(input()))
    
for tmp in combinations(li, 7):
    if sum(tmp) == 100: 
        li = list(tmp) 
        break 
    
# print('done')
li.sort()
for i in li:
    print(i)