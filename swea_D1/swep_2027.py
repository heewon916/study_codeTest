'''
출력
#++++
+#+++
++#++
+++#+
++++#
'''

for i in range(5):
    # print("+" * i, end='')
    # print("#" * 1, end='')
    # print("+" * (4-i))
    for j in range(i):
        print("+", end='')
    print("#", end='')
    for k in range(4-i):
        print("+", end='')
    print()