N = int(input())    #사람명수
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠
s_cnt = 0
for i in sizes:
    if i == 0:
        continue # 아무도 신청 안한 사이즈는 굳이 묶음 구매할 필요가 없다.
    elif i < T:
        s_cnt += 1
    elif i%T == 0:  # 딱 T의 배수일 때는 i//T 에 1을 더할 필요가 없다.
        s_cnt += i // T
    else: # i > T
        s_cnt += (i//T + 1)

# 펜
p1 = N // P
p2 = N % P

print(s_cnt)
print(p1, p2)