# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def is_even(a):
    return a % 2 == 0

def solve(n, x, y):
    if is_even(n):
        if is_even(x + y):
            return n // 2 * (x - 1) + (y + 1) // 2
        else:
            return n * n // 2 + n // 2 * (x - 1) + (y + 1) // 2
    else:
        if is_even(x + y):
            return (x - 1) // 2 * n + (n + 1) // 2 if is_even(x) else 0 + (y + 1) // 2
        else:
            return (n * n + 1) // 2 + (x - 1) // 2 * n + (n - 1) // 2 if is_even(x) else 0 + (y + 1) // 2

n, q = map(int, input().split())
for _ in range(q):
    x, y = map(int, input().split())
    print(solve(n, x, y))