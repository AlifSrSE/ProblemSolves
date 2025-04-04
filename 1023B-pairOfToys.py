# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, k = map(int, input().split())
    return max(0, min(n, k - 1) - ((k + 2) // 2) + 1)

print(solve())