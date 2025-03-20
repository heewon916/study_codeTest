n = int(input())
cmds = input()
nums = []
for _ in range(n):
    nums.append(int(input()))
#pt = 0
stk = []
for cmd in cmds:
    if cmd.isalpha():
        stk.append(nums[ord(cmd)-ord('A')])
        #stk.append(nums[pt])
        #pt += 1
    else:
        a = stk.pop()
        b = stk.pop()
        #print(f"about a{a}, b{b}")
        if cmd == "+":
            stk.append(a+b)
        elif cmd == "*":
            stk.append(a*b)
        elif cmd == "/":
            stk.append(b/a)
        elif cmd == "-":
            stk.append(b-a)
    #print(stk)
print(f"{stk[0]:.2f}")
