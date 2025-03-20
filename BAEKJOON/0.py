def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print('changed', arr[j], arr[j-1])
            print(arr)
        print('term', arr)
arr = [30, 15, 69, 14, 34, 45, 21, 23, 71, 33]

bubble_sort(arr)
print(arr)