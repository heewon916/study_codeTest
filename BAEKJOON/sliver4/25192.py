import sys
input = sys.stdin.readline
N = int(input().strip())
cnt = 0
dic = set()
# enter가 쳐지면, 앞에서 말했던 사람이어도 +1
for _ in range(N):
    str = input().rstrip()
    if str == "ENTER":
        dic.clear()
    else:
        if str not in dic:
            dic.add(str)
            cnt += 1
print(cnt)