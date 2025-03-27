# 지구 e 태양 s 달 m 
# 1-15  1-28  1-19
# 우리의 1년 = 1 1 1
# 1년 지나면 세 수 모두 +1;  넘어가면 1로 컴백 
E,S,M = map(int, input().split())
year = 1
e,s,m =1,1,1
while True: 
    if e==E and s==S and m==M:
        break 
    year += 1
    e += 1; s+=1; m+=1
    if e>15: e=1
    if s>28: s=1
    if m>19: m=1
    # print(year, e,s,m)
print(year)
### 다른 풀이
# e, s, m = map(int, input().split())
# all = 15 * 28 * 19
# x = (6916 * e + 4845 * s + 4200 * m) % all
# if x == 0:
#     x = all
# print(x)
###

# 15 15 15
# 1 16 16  -> 15 + 1
# 2 17 17
# 3 18 18 
# 4 19 19 
# 5 20 1 -> 19 + 1
# 6 21 2
# 7 22 3 
# 8 23 4
# 9 24 5
# 10 25 6
# 11 26 7
# 12 27 8
# 13 28 9 
# 14 1 10 -> 28 + 1