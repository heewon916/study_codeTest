# import sys
# sys.stdin = open("C:\\2024_CodeTest\\swep_D3\\swep1289_input.txt", "r")

T = int(input())
def getGroup(num):
    for y in range(200):
        start_num = 1 + y*(y-1)/2
        if num < start_num: 
            return y-1, 1+(y-1)*(y-2)/2
        
def getXY(num):
    start_y, start_num = getGroup(num)
    #print('num{} startY{} startNum{}'.format(num, start_y, start_num))
    dxdy = abs(start_num - num) 
    x = 1+dxdy
    y = start_y-dxdy
    #print('\tX{} Y{}'.format(x, y))
    return x,y

def getNum(rx,ry):
    dxdy = rx - 1
    group = ry + dxdy 
    start_num = 1 + group*(group-1)/2
    answer = start_num + dxdy
    return answer

for jc in range(1,T+1):
    p, q = map(int, input().split())
    
    px, py = getXY(p)
    qx, qy = getXY(q)
    
    #print(px, py, qx, qy)
    rx, ry = px+qx, py+qy 
    print('#{} {}'.format(jc, getNum(rx, ry)))
    
    
    