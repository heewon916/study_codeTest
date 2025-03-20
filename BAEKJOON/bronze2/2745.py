# 0-9 A-Z(10-35)

n, b = map(str, input().split())

# n -> 1의 자리부터 b^i로 곱한 걸 더해서 10진수로 
# b -> 2
total = 0 
b = int(b)
for i in range(len(n)-1, -1,-1):
    if n[len(n)-1-i].isalpha():
        total += (ord(n[len(n)-1-i]) - ord('A') + 10) * (b**i)
    else: 
        total += int(n[len(n)-1-i]) * (b**i)    
print(total)
            
# if b > 10: 
#     for i in range(len(n)-1, 0 ,-1):
#         if n[len(n)-1-i].isalpha():
#             total += (n[len(n)-1-i] - ord('A') + 10) * (b**i)
#         else: 
#             total += n[len(n)-1-i] * (b**i)    
# else: 
#     for i in range(len(n)-1, 0 ,-1):
#         total += n[len(n)-1-i] * (b**i)