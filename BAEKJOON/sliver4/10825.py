import sys
input = sys.stdin.readline

N = int(input().rstrip())
dic = {}
for _ in range(N):
    name, a,b,c = map(str, input().rstrip().split())
    dic[name] = (int(a), int(b), int(c))

# for x in dic.items():
#     print(x, x[0], x[1])
# 1번째 출력: ('Junkyu', (50, 60, 100)) Junkyu (50, 60, 100)
dic = dict(sorted(dic.items(), key=lambda x:(-x[1][0], x[1][1], -x[1][2], x[0])))
for k in dic.keys():
    print(k)