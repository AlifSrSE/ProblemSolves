# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1999/C
 
def solve(l, r, s, m):
    return any((m if i == len(l) else l[i]) - (0 if i == 0 else r[i - 1]) >= s for i in range(len(l) + 1))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, s, m = map(int, input().split())
        l = []
        r = []
        for _ in range(n):
            li, ri = map(int, input().split())
            l.append(li)
            r.append(ri)
        print("YES" if solve(l, r, s, m) else "NO")