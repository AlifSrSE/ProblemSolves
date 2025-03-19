# Author : AlifSrSE
# Date : 2025-03-18
# Problem link : https://codeforces.com/contest/1985/problem/E

def solve():
    x, y, z, k = map(int, input().split())
    ans = 0
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if k % (i * j) == 0:
                rest = k // (i * j)
                if rest <= z:
                    ans = max(ans, (x - i + 1) * (y - j + 1) * (z - rest + 1))
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()