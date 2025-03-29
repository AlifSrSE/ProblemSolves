# Author : AlifSrSE
# Date : 2025-03-29
# Problem link : https://codeforces.com/contest/2072/problem/A

def solve():
    n, k, p = map(int, input().split())
    if k < (-n * p) or k > (n * p):
        print(-1)
    else:
        ans = abs(k)
        print((ans // p) + (1 if ans % p else 0))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()