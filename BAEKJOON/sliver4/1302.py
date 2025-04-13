N = int(input())
dic = {}
for i in range(N):
    name = input()
    if name in dic:
        dic[name] += 1
    else: dic[name] = 1
dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(dic[0][0])
