import sys
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep1240_input.txt", "r")
dic = {"0001101":0, "0011001":1, "0010011":2,
       "0111101":3, "0100011":4, "0110001":5,
       "0101111":6, "0111011":7, "0110111":8,
       "0001011":9}
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    graph = [input() for _ in range(n)]
    arr = []
    for tmp in graph:
        if "1" in tmp:
            arr = tmp
            break
    codes = []
    # 암호코드 자르기
    for j in range(m-1, -1, -1):
        if arr[j] == '1':
            k = j # 암호코드 끝점 가져오기
            break

    # 암호코드 시작점 k-55 부터 k+1)-1=k까지 7개씩 끊기
    for s in range(k-55, k+1, 7):
        codes.append(dic[arr[s:s+7]])

    check = 0
    for a in range(4):
        check += codes[a*2]*3 + codes[a*2+1]

    if not check%10:
        print("#{} {}".format(tc, sum(codes)))
    else:
        print("#{} {}".format(tc, 0))
    # for i in range(0, len(arr), 7):
    #     if sum(arr[i:i+7]):
    #         codes.append("".join(map(str, arr[i:i+7])))
    # ans = ""
    # print(ans)
    # for code in codes:
    #     ans += str(dic[code])
    # res = 0
    # for i in range(len(ans)):
    #     if i%2 == 0:
    #         res += int(ans[i])
    #     else:
    #         tmp += int(ans[i])
    # res = res + tmp*3
    # print(res)
    # print("#{} {}".format(tc, res))



