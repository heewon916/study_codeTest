for _ in range(int(input())):
    dic = {}
    for i in range(int(input())):
        name, type_ = map(str, input().split())
        if type_ not in dic:
            dic[type_] = 1
        else: dic[type_] += 1
    total = 1
    for v in dic.values():
        total *= (v+1)
    print(total - 1)
