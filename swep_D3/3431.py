T = int(input())
for tc in range(1, T+1):
    l, u, x = map(int,input().split())
    # l분 이상 u분 이하
    # 현재 x분 진행함
    print(l-x if x>=l and x<=u else -1)