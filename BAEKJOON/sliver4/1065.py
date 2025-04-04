# 1-99는 모두 해당
# 101 111 123 135 147 159
# 121
N = int(input())
cnt = 0
for i in range(100, N+1):
    li = list((map(int, str(i))))
    if li[0]-li[1] == li[1]-li[2]:
        cnt += 1
        # print(i)
    # if abs(li[0]-li[1]) == abs(li[1]-li[2]):
    #     cnt += 1
        # print(i)
if N < 100:
    cnt = N
    # cnt = 99
else:
    cnt += 99
print(cnt)