x, y = map(int, input().split())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = ('MON, TUE, WED, THU, FRI, SAT, SUN').split(', ')
dayCount = y
for i in range(1, x):
    dayCount += days[i]

print(d[dayCount % 7-1])
# -1 넣어야 하는 이유: 1월 1일은 dayCount=1로 잡히므로 1을 빼줘야 한다.