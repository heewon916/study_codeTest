hexN = input() 
digit = 0 
for i in range(len(hexN)-1, -1, -1): 
    if hexN[i].isalpha(): 
        digit += (ord(hexN[i])-ord('A')+10)*(16**(len(hexN)-1-i))
    else: 
        digit += int(hexN[i]) * (16**(len(hexN)-1-i))
    # print(hexN[i], digit)
print(digit)