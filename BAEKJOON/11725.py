import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

# 누가 부모이고 자식인지는 아직 모른다.
# 따라서 연결 리스트로 양쪽에 다 저장해줘야 돼

linked = [[0] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    linked[u].append(v)
    linked[v].append(u)

parent = [0]  * (n+1) # 각 노드의 부모를 기록하자.
parent[1] = 0 # 루트니까 부모가 없다.

q = deque() # 1부터 시작해서, 자식들을 찾아나가는 걸로
q.append(1)

while q:
    current = q.popleft()
    for v in linked[current]: # 현재 정점이랑 연결된 것들에 대해서,
        if parent[v] == 0: # 부모가 아직 없을 때, current가 부모이다.
            parent[v] = current
            q.append(v)
    # print('q', q)

print('\n'.join(map(str, parent[2:])))