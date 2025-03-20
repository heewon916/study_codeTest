for ts in range(int(input())):
    r, s = map(str, input().split())
    ans = ''
    for i in s:
        ans += i*int(r)
    print(ans)