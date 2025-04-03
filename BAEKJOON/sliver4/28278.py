#N = int(input())
import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    n = sys.stdin.readline().split()
    # n, x = map(int, input().split(" "))
    if n[0] == "1":
        stack.append(n[-1])
    elif n[0] == "2":
        if stack: print(stack.pop())
        else: print("-1")
    elif n[0] == "3":
        print(len(stack))
    elif n[0] == "4":
        if stack: print("0")
        else: print("1")
    elif n[0] == "5":
        if stack: print(stack[-1])
        else: print("-1")
