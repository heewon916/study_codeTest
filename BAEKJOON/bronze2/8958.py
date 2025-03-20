for i in range(int(input())):
    string = input()
    ans = 0
    cnt = 0
    for c in string:
        if c == "X":
            cnt = 0  
            continue
        cnt += 1
        ans += cnt
    print(ans)