# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1296/problem/B

import sys

def alif():
    try:
        s = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    total = 0
    while s >= 10:
        spent_amount = (s // 10) * 10
        total += spent_amount
        s = (s // 10) + (s % 10)
    
    total += s
    print(total)

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()