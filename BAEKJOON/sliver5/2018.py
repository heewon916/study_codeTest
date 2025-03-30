N = int(input())
# li = [i for i in range(N+1)]
start, end = 0, 0
total, count = 0, 0
while end <= N: 
    if total < N: 
        end += 1
        total += end 
    elif total > N:
        total -= start
        start += 1
    else: 
        count += 1
        end += 1
        total += end
print(count)
        