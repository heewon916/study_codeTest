for ts in range(int(input())):
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    print(li[2])