# 0 1
# 1 2-7 6
# 2 8-19 12
# 3 20-37 18 
# 4 38-61
n = int(input())
end =1
group = 0

while n > end:
    group+=1
    end=end+(6*group if group>0 else 1)

print(group+1)