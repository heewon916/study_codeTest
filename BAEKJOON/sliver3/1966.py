from collections import deque
for _ in range(int(input())):
    N, M = map(int, input().split())
    score_q = deque((k,v) for k, v in enumerate(list(map(int, input().split()))))
    cnt = 0
    while score_q:
        max_v = max([v for k, v in score_q])
        i, score = score_q.popleft()
        # print("max-v = {}, ({}, {}), score_q = {} ".format(max_v, i, score, score_q))
        if score != max_v:
            score_q.append((i, score))
        else:
            cnt += 1
            if i == M:
                print(cnt)
                break
