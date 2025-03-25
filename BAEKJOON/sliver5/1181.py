li = []
for i in range(int(input())):
    li.append(input())

li = sorted(sorted(list(set(li))), key=lambda x:len(x))
for i in li:
    print(i)