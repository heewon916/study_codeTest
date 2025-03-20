from collections import deque
t = int(input())
for i in range(t):
    n, target = map(int, input().split()) #target이 몇 번째로 출력되는지를 알아야
    pri = list(map(int, input().split()))
    dic = dict()
    for i in range(n):
        dic[i] = pri[i]
    # q = deque(pri)
    q = deque(list(dic.items()))
    mx_t = max(q, key=lambda x:x[1])
    # idx = 0
    count = 0
    while q:
        mx_i, mx_n = mx_t
        q_i, q_n = q[0]
        if mx_n > q_n:
            q.append(q.popleft())
            # idx += 1
        elif mx_n == q_n:
            count += 1
            q.popleft()
            # mx = max(q)
            if mx_i == target:
                print(count)
                break
            mx_t = max(q, key=lambda x: x[1])
        print(q)







