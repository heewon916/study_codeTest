# 0-9 한 세트 
# 6 <-> 9
import math

li = list(map(int, input()))
# 6, 9 제외 몇번 나오는지 확인
cntList = [0 for i in range(10)]

for i in li:
    cntList[i] += 1

for69 = math.ceil((cntList[6] + cntList[9])/2)
forelse = max(cntList[:6] + cntList[7:9])

print(max(for69, forelse))