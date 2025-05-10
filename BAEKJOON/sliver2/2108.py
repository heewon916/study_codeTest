import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = [int(input().rstrip()) for _ in range(N)]

print(round(sum(li)/N))
print(sorted(li)[N//2])
countDic = {}
for c in li:
    if c in countDic:
        countDic[c] += 1
    else:
        countDic[c] = 1
countDic = sorted(countDic.items(), key=lambda x:(x[1], -x[0]), reverse=True)
if N > 1 and countDic[0][1] == countDic[1][1]:
    print(countDic[1][0])
else:
    print(countDic[0][0])
print(max(li)-min(li))