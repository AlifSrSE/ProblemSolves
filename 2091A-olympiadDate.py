# Author: AlifSrSe
# date: 2025-03-26
# https://codeforces.com/problemset/problem/2091/A
 
def solve():
    n = int(input())
    counts = [0] * 10
    ans = 0
    nums = list(map(int, input().split()))

    for i, num in enumerate(nums):
        counts[num] += 1
        if counts[0] >= 3 and counts[1] >= 1 and counts[2] >= 2 and counts[3] >= 1 and counts[5] >= 1 and ans == 0:
            ans = i + 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()