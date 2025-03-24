# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1980/C
 
def solve(a, b, d):
    if all(bi != d[-1] for bi in b):
        return False

    value_to_diff_count = {}
    for i in range(len(b)):
        if b[i] != a[i]:
            value_to_diff_count[b[i]] = value_to_diff_count.get(b[i], 0) + 1

    for i in range(len(d) - 1, -1, -1):
        if value_to_diff_count.get(d[i], 0) != 0:
            value_to_diff_count[d[i]] -= 1

    return all(diff_count == 0 for diff_count in value_to_diff_count.values())

if __name__ == "__main__":
    sc = int(input())
    for _ in range(sc):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        m = int(input())
        d = list(map(int, input().split()))
        print("YES" if solve(a, b, d) else "NO")