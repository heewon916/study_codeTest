# s = input()
# res = ''
# for i in range(1, len(s)-1):
#     for j in range(i+1, len(s)):
#         p1 = s[:i][::-1]
#         p2 = s[i:j][::-1]
#         p3 = s[j:][::-1]
        
#         combined = p1 + p2 + p3 
#         if len(res) == 0 or combined < res: 
#             res = combined
# print(res)
s = input()

sort_s = sorted(list((set(s)))) 

first = s.find(sort_s[0])
for i in range(1, len(sort_s)):
    second = s.find(sort_s[i])
    if second != -1 and first < second and second != len(s)-1: 
        break 

print(s[:first+1][::-1] + s[first+1:second+1][::-1] + s[second+1:][::-1])
