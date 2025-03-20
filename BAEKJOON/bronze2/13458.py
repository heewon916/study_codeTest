# n Ai 
# B*1 + C*a => a의 최솟값 

n = int(input())
li = list(map(int, input().split()))
b, c = map(int, input().split())

need = n*1
for p in li: 
    p = p-b if p>b else 0 
    if p>0: 
        need += (p//c) if p%c==0 else (p//c)+1
print(need)