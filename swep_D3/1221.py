import sys
sys.stdin = open("C:\\study_codeTest\\swep_D3\\swep1221_output.txt", "r")
T = int(input())
dic_map = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
z = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dic_map2 = {v:k for k, v in dic_map.items()}
for tc in range(1, T+1):
    t, case = map(str, input().split())
    arr = []
    lst = list(map(str, input().split()))
    for s in lst:
        arr.append(dic_map[s])
    arr.sort()
    print(f"#{tc}")
    for n in arr:
        print(dic_map2[n], end=" ")
