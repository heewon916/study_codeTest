import sys
INPUT = sys.stdin.readline

N = int(INPUT())
cards = list(map(int, INPUT().split()))
M = int(INPUT())
given = list(map(int, INPUT().split()))

# dic = dict.fromkeys(given)
cards.sort()
N_dic = {}
for n in cards:
    if n in N_dic:
        N_dic[n] += 1
    else:
        N_dic[n] = 1

def binary(n):
    low = 0
    high = len(cards)-1
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] == n:
            return N_dic[n]
        elif cards[mid] < n:
            low = mid + 1
        elif cards[mid] > n:
            high = mid - 1
    return 0

for m in given:
    print(binary(m), end =' ')

# for k in given:
#     ret = binary(k)
#     if ret:
#         count = 0
#         for i in range(ret, -1, -1):
#             if cards[i] == k: count += 1
#             else: break
#         for i in range(ret+1, N):
#             if cards[i] == k: count += 1
#             else: break
#         # dic[k] = count
#         print(count, end=' ')
#     else:
#         print(0, end=' ')
# for v in dic.values():
#     print(v, end = ' ')

