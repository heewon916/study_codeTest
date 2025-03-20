n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 꼭 dp 테이블을 선언하지 않아도 돼. 이 경우네느 arr 배열을 그대로 사용하는게 더 효율적이야.

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif j == len(arr[i])-1:
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = arr[i][j] + max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[n-1]))
