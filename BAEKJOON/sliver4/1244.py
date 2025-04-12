# 1 = on / 0 = off
# 남자 -> 자기가 받은 수의 배수인 스위치 번호에 대해 -> 상태 바꿈
# 여자 -> 자기 자신 i 기준; i-p과 i+p 값이 같을 경우 상태 바꾼다. 다를 경우 상태 안 바꾸고 stop.

N = int(input()) # 1번부터
S = list(map(int, input().split()))
st = int(input())
for _ in range(st):
    x, s = map(int, input().split())
    # print(x, s)
    if x == 1: #남자
        for i in range(s, N+1, s):
            S[i-1] = abs(S[i-1]-1)
    else: # 여자
        i = 1
        s = s - 1
        changelist = [s]
        while s-i>=0 and s+i<N:
            # 작업
            if S[s-i] == S[s+i]:
                changelist.append(s-i)
                changelist.append(s+i)
            else:
                break
            i += 1
        # print(changelist)
        for c in changelist:
            S[c] = abs(S[c]-1)
    # print("about",x,s, "result", S)

cnt = 1
for x in S:
    if cnt%20 == 0:
        print(x)
    else:
        print(x, end=' ')
    cnt += 1
