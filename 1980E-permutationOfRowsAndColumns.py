# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1980/E
 
def solve(a, b):
    n = len(a)
    m = len(a[0])

    value_to_old_r = {}
    value_to_old_c = {}
    for r in range(n):
        for c in range(m):
            value_to_old_r[a[r][c]] = r
            value_to_old_c[a[r][c]] = c

    r_mapping = {}
    for r in range(n):
        if value_to_old_r[b[r][0]] in r_mapping:
            return False
        r_mapping[value_to_old_r[b[r][0]]] = r

    c_mapping = {}
    for c in range(m):
        if value_to_old_c[b[0][c]] in c_mapping:
            return False
        c_mapping[value_to_old_c[b[0][c]]] = c

    for r in range(n):
        for c in range(m):
            if b[r_mapping[r]][c_mapping[c]] != a[r][c]:
                return False

    return True

if __name__ == "__main__":
    sc = int(input())
    for _ in range(sc):
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            a.append(list(map(int, input().split())))
        b = []
        for _ in range(n):
            b.append(list(map(int, input().split())))

        print("YES" if solve(a, b) else "NO")