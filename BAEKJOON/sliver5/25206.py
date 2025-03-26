grade = "A+ A0 B+ B0 C+ C0 D+ D0 F".split(' ')
s1 = s2 = 0 

for i in range(20):
    name, a, b = map(str, input().split())
    if b == "P":
        continue
    else:
        if b == "F":
            add = 0.0
        else: 
            add = float(a) * (4.5-grade.index(b)*0.5)
        s1 += add
        s2 += float(a)
    
print(s1 / s2)
    