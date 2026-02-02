# Author: AlifSrSE
import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1

    out = []

    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2

        grid = data[idx:idx+n]
        idx += n

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != '*':
                    continue

                ans += 1  # k = 0

                d = 1
                while True:
                    if (i-d < 0 or i+d >= n or
                        j-d < 0 or j+d >= m):
                        break
                    if (grid[i-d][j] == '*' and
                        grid[i+d][j] == '*' and
                        grid[i][j-d] == '*' and
                        grid[i][j+d] == '*'):
                        ans += 1
                        d += 1
                    else:
                        break

        out.append(str(ans))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
