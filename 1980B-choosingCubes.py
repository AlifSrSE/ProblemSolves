# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1980/B
 
def solve(a, f, k):
    if sum(1 for ai in a if ai > a[f - 1]) >= k:
        return "NO"
    if sum(1 for ai in a if ai >= a[f - 1]) <= k:
        return "YES"
    return "MAYBE"

if __name__ == "__main__":
    sc = int(input())
    for _ in range(sc):
        n, f, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, f, k))