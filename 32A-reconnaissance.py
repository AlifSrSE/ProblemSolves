# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/32/A

def solve():
    n, d = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort()

    total = 0
    for k in range(n):
        for m in range(k + 1, n):
            if height[m] <= height[k] + d:
                total += 1
            else:
                break

    print(2 * total)

if __name__ == "__main__":
    solve()