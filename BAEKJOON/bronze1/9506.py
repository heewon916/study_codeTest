import math 
while True: 
    n = int(input())
    if n == -1: 
        break 
    divs = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: 
            divs.append(i)
            divs.append(n//i)
    # print(divs)
    divs.sort()
    if sum(divs) == n: 
        print('{} = '.format(n), end='')
        for i in range(len(divs)): 
            if i == (len(divs)-1): 
                print(divs[i])
            else:
                print(divs[i], end=' + ')
    else: 
        print("{} is NOT perfect.".format(n))
    