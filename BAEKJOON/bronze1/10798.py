words = []
for i in range(5):
    tmp = input()
    words.append(tmp+(15-len(tmp))*' ')
    
# print(words)

for i in range(15):
    for j in range(5):
        if words[j][i] == ' ':
            continue
        else:
            print(words[j][i], end='')