n, b = map(int, input().split())
res = []
while n: 
    tmp = n % b 
    if b > 10 and tmp >= 10: 
        tmp = chr(tmp - 10 + ord('A'))
    # print(res, tmp)
    res.append(tmp)
    n = n // b 
# print(res)
print(''.join(map(str, res[::-1])))
# join() 반드시 모든 요소가 문자열이어야 한다. 숫자가 포함되면 TypeError 발생

## 다른 풀이 
# number='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# s=''
# while n:
#     s+=str(number[n%b])
#     n//=b

# print(s[::-1])