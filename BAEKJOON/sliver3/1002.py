# 조규현 좌표와 백승환 좌표 각각에서 류재명과의 거리 계산
# 있을 수 있는 좌표의 수 == 두 원의 교차점 개수
# 두 원의 중점과 반지름이 같으면 무한대, 안 만나면 0
import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    # 1. 완전히 같거나
    if x1 == x2 and y1 == y2 and r1 == r2: print(-1)
    # 2. 외접하거나 내접하거나
    elif distance == (r1+r2) or distance == abs(r1-r2): print(1)
    # 3. 원끼리 안 만날 때; 밖/ 안
    elif distance > (r1+r2) or distance < abs(r1-r2): print(0)
    # 4. 교차할 때
    else: print(2)