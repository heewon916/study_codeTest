import sys
input = sys.stdin.readline
while True:
    p = str(int(input()))
    if int(p) == 0: break
    low = 0
    high = len(p)-1
    while low <= high:
        # print(p[low], p[high])
        if p[low] != p[high]:
            print("no")
            break
        else:
            low += 1
            high -= 1
    else:
        print("yes")