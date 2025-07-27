T = 10

for t in range(1, T+1):
    N = int(input())
    h = list(map(int, input().split()))
    res = 0
    for i in range(2, len(h)-2):
        maxV = max(h[i-2], h[i-1], h[i+1], h[i+2])
        if h[i] >= maxV:
            res += h[i] - maxV
    print("#{} {}".format(t, res))