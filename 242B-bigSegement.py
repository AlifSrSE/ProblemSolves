# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

n = int(input())
segments = []
min_l = float('inf')
max_r = -float('inf')
candidate_index = -1

for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))
    if l < min_l:
        min_l = l
        max_r = r
        candidate_index = i + 1
    elif l == min_l:
        if r > max_r:
            max_r = r
            candidate_index = i + 1

candidate_l, candidate_r = segments[candidate_index - 1]
all_covered = True
for l, r in segments:
    if l < candidate_l or r > candidate_r:
        all_covered = False
        break

if all_covered:
    print(candidate_index)
else:
    print(-1)