import sys
input = sys.stdin.readline
N = int(input().rstrip())
dic = {}
for _ in range(N):
    a = int(input().rstrip())
    if a not in dic: dic[a] = 1
    else: dic[a] += 1

dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(dic[0][0])