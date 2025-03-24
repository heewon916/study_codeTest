n = int(input())
words = []
same = 0
res = ''
for i in range(n):
    words.append(input())
    
for chars in zip(*words):
    # print(chars)
    if len(set(chars)) == 1: 
        res += chars[0]
    else: 
        res += '?'
        
print(res)
# for i in range(len(words[0])):
#     tmp = words[0][i]
#     for j in range(1, n):
#        if tmp == 