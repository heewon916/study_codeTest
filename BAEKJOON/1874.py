n = int(input())
stack = []
ops = []
add = 1
able = True
for i in range(n):
    x = int(input())
    while add <= x:
        stack.append(add)
        ops.append('+')
        add += 1
    if stack[-1] == x:
        stack.pop()
        ops.append('-')
    else:
        able = False
        break
if able:
    for i in ops:
        print(i)
else:
    print("NO")



