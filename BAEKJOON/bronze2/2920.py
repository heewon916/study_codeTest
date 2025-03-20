string = ''.join(list(map(str, input().split(' '))))
if '12345678' == string: 
    print('ascending')
elif string == '87654321':
    print('descending')
else:
    print('mixed')
