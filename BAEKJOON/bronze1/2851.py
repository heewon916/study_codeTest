#처음부터 먹는데,
#도중에 중단하면, 그 뒤는 아예 먹을 수 없다. 

total = 0 
for i in range(10):
    n = int(input())
    if abs(total-100) >= abs(total+n-100):
        total += n 
    else: 
        break 
print(total)