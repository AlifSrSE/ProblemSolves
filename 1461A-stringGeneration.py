# Author: AlifSrSE
import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())

        if k == 1:
            s = []
            chars = "abc"
            for i in range(n):
                s.append(chars[i % 3])
            print("".join(s))
        else:
            pattern = "aab"
            print((pattern * ((n + 2) // 3))[:n])

if __name__ == "__main__":
    solve()
