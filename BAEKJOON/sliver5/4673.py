# d(n) = n + sum(list(map(int ,str(n))))
# 33 39 51 57 .. 
# 33은 39의 생성자 
# 셀프넘버 1 3 5 7 9 20 ...
# 모든 숫자에 대해 d(n) 계산 
li = []
for i in range(1, 10001):
    dn = i + sum(list(map(int, str(i))))
    li.append(dn)
    # print(dn)
    
for i in range(1, 10001):
    if i not in li:
        print(i)