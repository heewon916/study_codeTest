string = input()
ans = []
for i in range(26):
    ans.append(string.find(chr(i+ord('a'))))
for i in ans:
    print(i)