import sys
input = sys.stdin.readline
string = input().rstrip()
set_ = set()
for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        if string[i:j] != '':
            set_.add(string[i:j])

print(len(set_))