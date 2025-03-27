import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

print(li[k-1])

