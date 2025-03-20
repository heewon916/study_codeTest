N = int(input())

for i in range(1, N+1):
    num = sum(list(map(int, str(i))))
    num_sum = num + i
    if num_sum == N:
        print(i)
        break
    if i == N:
        print(0)
