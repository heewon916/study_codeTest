import sys 
input = sys.stdin.readline
li = []
for i in range(int(input())):
    age, name = map(str, input().split())
    li.append((int(age), name))
    # li.append((age, name))
for a, b in sorted(li, key=lambda x:x[0]):
    print('{} {}'.format(a, b))