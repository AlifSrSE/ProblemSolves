# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    f = {}
    for x in a:
        f[x] = f.get(x, 0) + 1
    more = [x for x, y in f.items() if y > 1]
    more.sort(reverse=True)
    found = False
    for i in range(n - 1):
        A = a[i]
        C = a[i + 1]
        bound = (C - A) // 2 + 1
        f[A] -= 1
        f[C] -= 1
        for x in more:
            if x < bound:
                break
            if f.get(x, 0) < 2:
                continue
            print(A, C, x, x)
            found = True
            break
        f[A] += 1
        f[C] += 1
        if found:
            break
    if not found:
        print("-1")

t = int(input())
for _ in range(t):
    solve()