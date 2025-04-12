N, K = map(int, input().split())
del_list = []
cnt = 0
for P in range(2, N+1):
    for x in range(P, N+1, P):
        if x not in del_list:
            del_list.append(x)
print(del_list[K-1])
