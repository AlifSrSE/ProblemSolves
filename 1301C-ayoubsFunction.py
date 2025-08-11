# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1301/problem/C

import sys

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str:
            return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n, m = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            continue

        a = (n - m) // (m + 1)
        b = (n - m) % (m + 1)
        total_subarrays = n * (n + 1) // 2
        zero_subarrays = (m + 1) * a * (a + 1) // 2 + b * (a + 1)
        ans = total_subarrays - zero_subarrays
        
        print(ans)

if __name__ == "__main__":
    main()