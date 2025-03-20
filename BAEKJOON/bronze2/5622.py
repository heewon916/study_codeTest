endL = list('CFILOSVZ')
default = 3
ans = 0 
for c in input():
    for i in range(len(endL)):
        if c <= endL[i]:
            ans += i + default     
            break

print(ans)
            