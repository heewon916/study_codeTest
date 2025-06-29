# n개 중 m개 고르기 + 중복 가능 + 비내림차순 정렬
# 중복 조합
# 중복되는 수열은 출력 불가
# 라이브러리 없이 작성하는 법: 백트래킹
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = set()

def backtracking(curr_seq, start_idx):
    if len(curr_seq) == m:
        res.add(tuple(curr_seq))
        return
    for i in range(start_idx, n):
        curr_seq.append(arr[i])
        backtracking(curr_seq, i)
        curr_seq.pop()

backtracking([], 0)
for seq in sorted(list(res)):
    print(' '.join(map(str, seq)))
