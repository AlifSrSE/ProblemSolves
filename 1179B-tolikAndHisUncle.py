# Author: AlifSrSE 
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/1179/problem/B

def solve():
    n, m = map(int, input().split())
    if (n * m) % 2 == 1:
        print(-1)
        return

    result = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            for j in range(1, m + 1):
                result.append((i, j))
        else:
            for j in range(m, 0, -1):
                result.append((i, j))

    for x, y in result:
        print(f"{x} {y}")

if __name__ == "__main__":
    solve()