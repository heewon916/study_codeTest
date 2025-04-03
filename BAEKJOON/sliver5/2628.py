W, H = map(int, input().split())
# W 가로 H 세로
N = int(input())
wCut = []
hCut = []
for _ in range(N):
    a, n = map(int, input().split())
    if a == 1: # 세로
        hCut.append(n)
    elif a == 0:
        wCut.append(n)
wCut.sort()
hCut.sort()
if len(wCut) == 0: 
    wMax = H
else: 
    wMax = wCut[0]
    for i in range(1, len(wCut)):
        wMax = max(wMax, wCut[i]-wCut[i-1])
    wMax = max(wMax, H-wCut[-1])

if len(hCut) == 0: 
    hMax = W
else: 
    hMax = hCut[0]
    for i in range(1, len(hCut)):
        hMax = max(hMax, hCut[i]-hCut[i-1])
    hMax = max(hMax, W-hCut[-1])

print(wMax * hMax)