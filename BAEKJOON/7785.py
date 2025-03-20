n = int(input())
peo_map = {}
for _ in range(n):
    name, log = map(str, input().split())
    if log == "enter":
        peo_map[name] = 1
    else:
        del peo_map[name]

arr = sorted(peo_map.keys(), reverse=True)
for i in arr:
    print(i)


