for ts in range(int(input())):
    tmp = list(input().split())
    for i in range(len(tmp)): 
        tmp[i] = tmp[i][::-1]    
    print(' '.join(map(str, tmp)))
    