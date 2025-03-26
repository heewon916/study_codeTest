s = []
for i in range(int(input())):
    cmd = input()
    if cmd == "all":
        s = [i for i in range(1, 21)]
    elif cmd == "empty":
        s = []
    else: 
        op, x = map(str, cmd.split())
        x = int(x)
        if op == "add":
            if x not in s:
                s.append(x)
        elif op == "remove":
            try: 
                s.remove(x)
            except:
                continue 
        elif op == "check":
            if x in s: print(1)
            else: print(0)
        elif op == "toggle":
            if x in s: s.remove(x)
            else: s.append(x)

                
    