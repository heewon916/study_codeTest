T = int(input())

tr = []
for i in range(46):
    tr.append(i*(i+1)//2)

def isvalid(n):
    for i in range(1,46):
        for j in range(1, 46):
            for k in range(1, 46):
                if tr[i] + tr[j] + tr[k] == n:
                    return 1
    return 0
for tc in range(1, T+1):
    num = int(input())
    print(isvalid(num))

