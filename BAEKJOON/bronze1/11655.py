string = input()
res = ''
for c in string: 
    if c.isalpha():
        if c == c.upper(): 
            # WRONG!! tmp = chr((ord(c) + 13)%26 + ord('A')) 
            tmp = chr((ord(c)-ord('A') + 13)%26 + ord('A'))
        elif c == c.lower():
            tmp = chr((ord(c)-ord('a') + 13)%26 + ord('a'))
        res += tmp 
        # print(c, res)
    else: 
        res += c
print(res)