# dz= lj nj 하나로 볼 것 
li = list("c= c- dz= d- lj nj s= z=".split())

string = input()
for c in li:
    string = string.replace(c, "*")
    # print(string)
print(len(string))
# for c in li:
#     for i in range(len(li)):
#         pos = string.find(c, i)
#     string = string.replace(c, "_"*len(c))
#         if pos != -1:
#             print(string[i:], c)
#             count += 1