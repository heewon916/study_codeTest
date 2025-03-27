# 0001100
# 1110011 => 1번
# 000111 => 1번
# 101010 => 결국 3번 
# 연속하는가를 체크
# 애초에 문자열 받을 때, 값이 같은 것끼리 묶기

s = input()
li = []
tmp = ''
for c in s:
    if len(tmp) == 0:
        tmp = c    
        continue
    if tmp[-1] == c:
        tmp += c
    else: 
        li.append(tmp)
        tmp = c
li.append(tmp)
# print(li)
for i in range(len(li)): 
    li[i] = list(set(li[i]))[0]
# print(li)

print(min(li.count('0'), li.count('1')))

## 다른 풀이 
s = input()
print(s.split('0'), s.split('1'))
# ['111', '', '11'] ['', '', '', '00', '', '']
one = [x for x in s.split('0') if x != '']
zero = [x for x in s.split('1') if x != '']
print(min(len(one), len(zero)))