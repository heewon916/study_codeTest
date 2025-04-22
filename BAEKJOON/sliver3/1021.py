from collections import deque
N, M = map(int, input().split())

q = deque([i for i in range(1, N+1)])

# 뽑고자 하는 위치는 왼쪽에서 1부터 센다.
popList = list(map(int, input().split()))
count = 0  # 2번, 3번 연산 횟수
# 뽑아낼 수 있는 곳은 왼쪽 뿐이다. 뽑을 위치를 항상 왼쪽으로 옮겨야 한다.
for i in range(M):
    pop_pt = q.index(popList[i])

    if pop_pt == 0:
        q.popleft()
    elif pop_pt > len(q)//2:
        for _ in range(len(q)-pop_pt):
            q.appendleft(q.pop())
            count += 1
        q.popleft()
    else:
        for _ in range(pop_pt):
            q.append((q.popleft()))
            count += 1
        q.popleft()
print(count)