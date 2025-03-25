# 1 
# 2 3 
# 4 5 6
# 몇 번째 그룹에 속하는지 

x = int(input())
end = group = 1
while True: 
    if x <= end: 
        break 
    else:
        group += 1
        end += group
        # print(group, end)
# print(x, end, group)

if group%2 == 0:
    a, b = 1, group
    for i in range(x - (end-group+1)):
        a += 1
        b -= 1
else:
    a, b = group, 1
    for i in range(x - (end-group+1)):
        a -= 1 
        b += 1
print("{}/{}".format(a, b))