# 하루에 올라갈 수 있는 거리 a-b
# 올라가야 하는 거리 v-b
# 마지막 날 미끄러지는 것 감안하면 안되니, 결국 v-b만큼 올라가는 것과 같다. 
# 따라서, (v-b)//(a-b) + 1
a, b, v = map(int, input().split())
print((v-b-1)//(a-b)+1)
# days = v//(a-b)
# if v%(a-b):
#     days += 1

# h = 0
# while True: 
#     h = h + a 
#     days += 1
#     if h >= v: 
#         break 
#     else: 
#         h = h - b 
