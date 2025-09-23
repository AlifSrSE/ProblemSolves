# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    possible = True
    for r in range(n):
        if not possible:
            break
        for c in range(m):
            d = (r > 0) + (c > 0) + (r < n - 1) + (c < m - 1)
            if a[r][c] > d:
                possible = False
                break
            else:
                a[r][c] = d
    if possible:
        print("YES")
        for r in range(n):
            print(*a[r])
    else:
        print("NO")
