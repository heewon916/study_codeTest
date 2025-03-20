import sys
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep5356_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]
    ans = ""
    max_len = 0
    for i in arr:
        max_len = max(len(i), max_len)

    for i in range(max_len):  # 최대 길이로 돌린다.
        for j in range(5):  # 각 문자열에 대해서
            if i < len(arr[j]):
                ans += arr[j][i]

            # try:
            #     ans += arr[j][i]
            # except:
            #     continue
    print("#{} {}".format(tc, ans))