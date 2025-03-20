N, L = map(int, input().split())
holes = list(map(int, input().split()))
covered = [0 for _ in range(len(holes))]
holes.sort()

count = 0
for i, h in enumerate(holes):
    able = [(h-0.5), (h-0.5) + L] # 커버 가능한 범위
    if not covered[i]:
        covered[i] = 1
        count += 1
        for j in range(i+1, len(holes)):
            if able[0] < holes[j] < able[1]:
                covered[j] = 1
    else:
        continue

print(count)