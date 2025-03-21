n = ans = int(input())
cnt = 0

while True:
    cnt += 1
    if n < 10: 
        add = 0 + n 
    else: 
        add = int(str(n)[0]) + int(str(n)[1])
    next = str(n)[-1]+ str(add)[-1]
    # print(cnt, n, add, next)
    if int(next) == ans: 
        break 
    else: 
        n = int(next) 
        
print(cnt)