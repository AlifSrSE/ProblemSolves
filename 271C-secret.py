# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/271/C

def solve():
    n, k = map(int, input().split())
    if n < 3 * k:
        print("-1")
    else:
        result = []
        for p in range(k):
            result.append(str(1 + (p + 1) % k))
        for p in range(k, n):
            result.append(str(1 + p % k))
        print(" ".join(result))

if __name__ == "__main__":
    solve()