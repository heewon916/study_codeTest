import heapq as hq
n = int(input())
a = list(map(int, input().split()))
ans = 0



# for i in range(n):
#     dp = [a[i]]
#     hp = []
#     pt = 0
#     for j in range(i+1, n):
#         tmp = dp[pt] + a[j]
#         dp.append(tmp)
#         hq.heappush(hp, -tmp)
#         pt += 1
#     # print(dp)
#     # print(hp)
#     ans = max(ans, -hp[0] if hp else 0)
# print(ans)