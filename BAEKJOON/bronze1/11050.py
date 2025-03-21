n, r = map(int, input().split())
top = 1; bottom = 1
for i in range(r):
    top *= n
    n -= 1
for i in range(r):
    bottom *= r
    r -= 1
    
print(top//bottom)