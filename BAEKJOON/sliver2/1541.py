import re
li = re.split('(-)', input())
res = 0
minus = False
for i in range(len(li)):
    if li[i] == '':
        continue
    elif li[i] == '-':
        minus = True
        continue
    else:
        # print(li[i].split("+"))
        if minus:
            res -= sum(map(int, li[i].split("+")))
        else:
            res += sum(map(int, li[i].split("+")))
        minus = False
    # print(li[i], res)
print(res)