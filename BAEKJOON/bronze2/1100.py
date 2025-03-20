cnt = 0
for i in range(8):
    board = list(input())
    if i%2 == 0: # 짝수 
        for j in range(0, 8, 2):
            if board[j] == "F": cnt+=1 
    else: # 홀수 
        for j in range(1, 8, 2):
            if board[j] == "F": cnt += 1
print(cnt)