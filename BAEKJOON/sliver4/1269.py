import sys
input = sys.stdin.readline
na, nb = map(int, input().rstrip().split())

# 1. intersection
A = set(list(map(int, input().rstrip().split())))
B = set(list(map(int, input().rstrip().split())))

print(na+nb - len(A.intersection(B))*2)
