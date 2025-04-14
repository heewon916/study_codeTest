# 가로수들이 모두 같은 간격이 되도록
# 가능한 적은 수의 나무
import sys
input = sys.stdin.readline

N = int(input().rstrip())
li = [int(input().rstrip()) for _ in range(N)]
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
dist = []
for i in range(N-1):
    d = abs(li[i]-li[i+1])
    dist.append(d)
# 1 4 7 10 처럼 전부 3만 차이날 때는, dist = [3]이 되는데,
# 이 경우 아래의 for문이 돌아가지 않을 수 있다. 따라서 중복 제외는 하지 않는다.
# for i in range(N - 1):
#     d = abs(li[i] - li[i + 1])
#     dist.append(d)
#     if d not in dist:
#           dist.append(d)

cur_gcd = dist[0]
for d in dist[1:]:
    cur_gcd = gcd(cur_gcd, d)
# 최대공약수를 구하기 위해서 max 연산을 하는 것도 좋지만,
# 결국 어떤 수와 공약수를 구하든, max 연산은 크게 의미가 없다. 왜냐면 gcd 함수 자체에서 최대공약수를 구하기 때문이다. 따라서 위와 같이 수정하는 것이 옳다.
# for i in range(len(dist)-1):
#     max_gcd = max(max_gcd, gcd(dist[i], dist[i+1]))
total = (li[-1] - li[0]) // cur_gcd + 1 # 총 필요한 나무의 개수
print(total - N )
##### # 문제점
# ## 아래와 같이 계산할 경우, 메모리 초과가 발생할 수 있다. 10^5개까지 배열이 주어질 수 있는데, int형 배열이므로 기본적으로 10^5 * 4byte를 사용한다.
# # 제한은 128MB = 128 * 1024KB = 128 * 1024 * 1024 Byte 이다.
# # 근데, 아래의 li2 선언문에서, cur_gcd = 1이 되고, li[-1] = 10^9이라면, 10억개의 리스트를 만들게 된다. 이때 int형 배열이므로 4byte * 10억 => 메모리 초과가 발생할 수밖에 없다.
# # 그리고, 기존의 li에 대해서 gcd를 나무 간격으로 해서 재생성하고
# li2 = [i for i in range(li[0], li[-1]+1, cur_gcd)]
#
# # 추가해야 하는 가로수의 개수를 구하면 된다.
# print(len(li2) - len(set(li2).intersection(set(li))))