# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2055/problem/B

def solve(a, b):
    diffs = [b[i] - a[i] for i in range(len(a))]
    positive_indices = [i for i, diff in enumerate(diffs) if diff > 0]

    return not positive_indices or (
        len(positive_indices) == 1 and all(
            i == positive_indices[0] or -diffs[i] >= diffs[positive_indices[0]] for i in range(len(diffs))
        )
    )

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES" if solve(a, b) else "NO")