# octN = input()
# total = 0 
# # 10진수로 
# for i in range(len(octN)):
#     total += int(octN[i]) * (8**(len(octN)-1-i))

# #2진수로 
# bin = ''
# while total != 0: 
#     bin += str(total % 2)
#     total = total // 2
    
# print(bin[::-1])

# bin() 함수를 사용해 맨 앞에 붙는 "0b"만 제거하고 리턴
print(bin(int(input(),8))[2:])