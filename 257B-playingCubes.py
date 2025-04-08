# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, m = map(int, input().split())
    print(f"{m + n - 1 - min(m,n)} {min(m,n)}")
solve()