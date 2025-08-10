# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1295/problem/A

import sys

def alif():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n = int(sys.stdin.readline())
        except (IOError, ValueError):
            continue

        result = ""
        if n % 2 == 1:
            result += "7"
            n -= 3

        num_ones = n // 2
        result += "1" * num_ones

        print(result)

if __name__ == "__main__":
    alif()