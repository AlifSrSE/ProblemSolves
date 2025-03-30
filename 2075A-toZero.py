# Author : AlifSrSE
# Date : 2025-03-30
# Problem link : https://codeforces.com/contest/2075/problem/A

def solve():
    n, k = map(int, input().split())
    ans = 0
    if n % 2:
        n -= k
        ans += 1
    ans += n // (k - 1)
    n %= (k - 1)
    if n:
        ans += 1
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()