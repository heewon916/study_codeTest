# 나보다 작은 좌표 개수; 중복 제외
import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = list(map(int, input().rstrip().split()))

countLi = sorted(list(set(li)))
dic = dict.fromkeys(li)
for i in range(len(countLi)):
    dic[countLi[i]] = i
for n in li:
    print(dic[n], end=' ')