import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0
for i in range(N):
    li = list(map(str, input().rstrip()))
    stk = []
    for c in li:
        stk.append(c)
        # print(c, stk)
        if len(stk)>1 and stk[-1]==stk[-2]:
            stk.pop()
            stk.pop()
    if len(stk)==0: cnt += 1
print(cnt)