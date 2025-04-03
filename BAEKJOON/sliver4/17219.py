N, M = map(int, input().split())

pwd = {}
for _ in range(N):
    site, pw = map(str, input().split())
    pwd[site] = pw

for _ in range(M):
    toFind = input()
    print(pwd[toFind])