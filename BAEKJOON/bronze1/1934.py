# 최소 공배수 

# 6 10 
# 6 = 2 x 3 
# 10 = 2 x 5

# 12 16 
# 12 = 2^2 x 3
# 16 = 2^4 
# => 최대 제곱으로 가야 함 

# # 1. 소인수 찾고 겹치는 거 빼고 다 곱하기 
# def find_factors(num):
#     factors = {}
#     while num%2 == 0:
#         num //= 2
#         if 2 not in factors:
#             factors[2] = 1
#         else: 
#             factors[2] += 1
#         # factors.append(2)
#     i = 3
#     while i*i <= num: 
#         while num%i == 0: 
#             num //= i 
#             if i not in factors:
#                 factors[i] = 1
#             else: 
#                 factors[i] += 1
#             # factors.append(i)
#         i += 1
#     if num > 1: 
#         factors[num] = 1
#         # factors.append(num)
        
#     return factors

# for ts in range(int(input())):
#     a, b = map(int, input().split())
#     factorsA = find_factors(a)
#     factorsB = find_factors(b) 
#     # print(factorsA, factorsB)
#     for i in factorsA:
#         if i in factorsB: 
#             factorsA[i] = max(factorsA[i], factorsB[i]) # 최소공배수 구하는 법 
#             # if factorsA[i] > factorsB[i]: ## 최대공약수 구하는 법
#             #     factorsA[i] = factorsB[i]
#     for i in factorsB:
#         if i not in factorsA: 
#             factorsA[i] = factorsB[i]
#     # print(factorsA)
#     result = 1
#     for k, v in factorsA.items():
#         result *= (k**v)       
#     print(result) 
#     # print((factorsB - factorsA) | (factorsA - factorsB) | factorsA.intersection(factorsB) | factorsB.intersection(factorsA))
    
# 2. gcd 활용 
def gcd(a, b): # 최대공약수 찾기 
    while b:
        a, b = b, a%b 
    return a
def lcm(a,b):
    return (a*b) // gcd(a,b)

for ts in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a,b))