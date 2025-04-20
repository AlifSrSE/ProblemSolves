# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# link : https://codeforces.com/contest/1501/problem/A

def solve():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    d = list(map(int, input().split()))

    t = 0
    depart = 0
    for p in range(n):
        prev_b = b[p - 1] if p > 0 else 0
        t = depart + (a[p] - prev_b + d[p])
        depart = t + (b[p] - a[p] + 1) // 2
        depart = max(depart, b[p])

    print(t)

num_test_cases = int(input())
for _ in range(num_test_cases):
    solve()