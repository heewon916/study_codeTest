# A의 위치를 이동하면서 최소 차이가 나는 곳에 위치시키고
# 채워지는 문자는 B와 무조건 똑같이 하면 된다.
# 기존의 A와 B의 최소 차이를 알아야 한다.

A, B = input().split()
min_diff = 51

for i in range(0, len(B)-len(A)+1, 1):
    tmp = B[i:i+len(A)]
    cnt = 0
    for a,b in zip(A, tmp):
        if a != b: cnt += 1
    min_diff = min(min_diff, cnt)
    # print(tmp, A, min_diff)
print(min_diff)