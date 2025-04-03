import sys
n = int(sys.stdin.readline())
n_s = list(map(int, sys.stdin.readline().split()))
n_s.sort()
m = int(sys.stdin.readline())
m_s = list(map(int, sys.stdin.readline().split()))

# def binary(i, low, high):
#     global n_s
#     while low <= high:
#         mid = (low + high) // 2
#         if n_s[mid] == i:
#             return 1
#         elif n_s[mid] < i:
#             binary(i, mid+1, high)
#         elif n_s[mid] > i:
#             binary(i, low, mid-1)
#     return 0

for m in m_s:
    # print(binary(m, 0, n-1))
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if n_s[mid] == m:
            print(1)
            break
        elif n_s[mid] < m:
            low = mid + 1
        elif n_s[mid] > m:
            high = mid - 1
    else:
        print(0)