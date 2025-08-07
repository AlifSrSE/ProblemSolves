# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1281/A

import sys

def solve():
    t = int(sys.stdin.readline())

    for _ in range(t):
        s = sys.stdin.readline().strip()
        ans = ""

        if s.endswith('o'):
            ans = "FILIPINO"
        elif s.endswith('u'):
            ans = "JAPANESE"
        elif s.endswith('a'):
            ans = "KOREAN"

        sys.stdout.write(ans + "\n")

if __name__ == "__main__":
    solve()