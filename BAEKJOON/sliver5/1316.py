count = 0 
for i in range(int(input())):
    string = input()
    dic = dict.fromkeys(string, 0)
    # 전에 마주치고 끝난 게 재등장 안됨.
    prev = ''
    flag = 1
    for c in string: 
        if prev != c:
            if dic[c] == 1: 
                flag = 0
                break 
            prev = c
            dic[c] = 1
    
    if flag == 1: 
        count += 1
    
    # print(string, count)
print(count)