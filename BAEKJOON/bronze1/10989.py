# 숫자 하나씩 받는대로 정렬을 해야 할 것 같다. 
# 힙트리 -> 중위순회 
# 버블, 선택, 삽입 -> n^2 데이터 양 너무 많다 
# 퀵, 병합, 힙 -> nlogn 데이터 양 너무 많다. 
# 계수정렬 -> 각 숫자의 갯수를 세어주는 방식. 숫자의 범위가 제한적이고 큰 수의 데이터를 정렬해야 할 때 매우 효율적이다. 
# import heapq

import sys

def input():
    return sys.stdin.readline()

n = int(input())
count = [0] * 10001

for i in range(n):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    if count[i] != 0: 
        for j in range(count[i]):
            print(i)