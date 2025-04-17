tc = int(input())
for _ in range(tc):
    dic = dict()
    n = int(input())
    for _ in range(n):
        name, type = map(str, input().split())
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1
    ans = 1
    for v in dic.values():
        ans *= (1 + v)
    print(ans-1)