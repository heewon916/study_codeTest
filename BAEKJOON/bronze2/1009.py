for ts in range(int(input())):
    a, b = map(int, input().split())
    data = a ** b 
    print(data % 10)