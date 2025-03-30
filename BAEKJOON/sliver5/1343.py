arr = list(input().split('.'))
result = []
for i in arr: 
    if len(i) == 2:
        result.append("BB")
    elif len(i) == 4: 
        result.append("AAAA")
    elif (len(i)%4)%2 == 0: 
        tmp = ''
        while len(i) > 0:
            if len(i) >= 4: 
                i = i.replace('XXXX', '',1)
                tmp += 'AAAA'
            else: 
                i = i.replace('XX','', 1)
                tmp += 'BB'
        result.append(tmp)
    else: 
        print(-1)
        break 
else: 
    print('.'.join(result))