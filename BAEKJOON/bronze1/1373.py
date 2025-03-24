binary = input()
res = ''
if len(binary)%3 != 0:
    binary = (3-len(binary)%3)*'0' + binary 
    
# print(binary)
    
for i in range(0, len(binary), 3):
    tmp = 0
    for j, c in enumerate(map(int, binary[i:i+3])):
        tmp += c * (2**(2-j))
    res += str(tmp)
    # print(tmp, res)
    
print(res)