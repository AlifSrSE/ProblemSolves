# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# link : https://codeforces.com/contest/1501/problem/B

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    rem = 0
    for p in range(n - 1, -1, -1):
        rem = max(rem, a[p])
        a[p] = 1 if rem > 0 else 0
        rem -= 1

    print(*a)

num_test_cases = int(input())
for _ in range(num_test_cases):
    solve()