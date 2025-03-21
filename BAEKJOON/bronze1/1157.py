dic = dict()
string = input().upper()
for c in string:
    if c not in dic:
        dic[c] = 1
    else: 
        dic[c] += 1

dic = list(sorted(dic.items(), key=lambda x: x[1], reverse=True))
# print(dic)
if len(dic) > 1:
    if dic[0][1] > dic[1][1]:
        print(dic[0][0])
    else:
        print("?")
else: 
    print(dic[0][0])
    
